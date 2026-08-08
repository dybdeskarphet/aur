#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import urllib.parse
import urllib.request


def parse_pkgbuild(pkg_dir: Path) -> dict:
    pkgbuild = pkg_dir / "PKGBUILD"
    if not pkgbuild.exists():
        return None

    content = pkgbuild.read_text(encoding="utf-8")

    pkgver_match = re.search(r"^pkgver=(.+)$", content, re.MULTILINE)
    pkgrel_match = re.search(r"^pkgrel=(.+)$", content, re.MULTILINE)
    desc_match = re.search(r"^pkgdesc=['\"](.+)['\"]$", content, re.MULTILINE) or re.search(
        r"^pkgdesc=(.+)$", content, re.MULTILINE
    )

    pkgver = pkgver_match.group(1).strip("'\"") if pkgver_match else "unknown"
    pkgrel = pkgrel_match.group(1).strip("'\"") if pkgrel_match else "1"
    desc = desc_match.group(1).strip("'\"") if desc_match else ""

    return {
        "name": pkg_dir.name,
        "repo_ver": f"{pkgver}-{pkgrel}",
        "desc": desc,
    }


def fetch_aur_info(pkg_names: list[str]) -> dict[str, str]:
    if not pkg_names:
        return {}

    query_params = "&".join(
        f"arg[]={urllib.parse.quote(name)}" for name in pkg_names
    )
    url = f"https://aur.archlinux.org/rpc/v5/info?{query_params}"

    req = urllib.request.Request(url, headers={"User-Agent": "aur-monorepo-readme-updater"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("results", [])
            return {item["Name"]: item.get("Version", "N/A") for item in results}
    except Exception as e:
        print(f"Warning: Failed to query AUR RPC API: {e}", file=sys.stderr)
        return {}


def generate_markdown_table(packages: list[dict], aur_info: dict[str, str]) -> str:
    lines = [
        "| Package | Description | Repo Version | AUR Version | Status |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for pkg in sorted(packages, key=lambda x: x["name"]):
        name = pkg["name"]
        repo_ver = pkg["repo_ver"]
        aur_ver = aur_info.get(name, "Not Published")
        desc = pkg["desc"]

        if aur_ver == "Not Published":
            status = "⚪ Not on AUR"
        elif repo_ver == aur_ver:
            status = "🟢 In-Sync"
        else:
            status = "🔴 Out-of-Date"

        aur_link = f"https://aur.archlinux.org/packages/{name}"
        lines.append(
            f"| [**{name}**]({aur_link}) | {desc} | `{repo_ver}` | `{aur_ver}` | {status} |"
        )

    return "\n".join(lines)


def update_readme(repo_root: Path):
    template_path = repo_root / "README_TEMPLATE.md"
    readme_path = repo_root / "README.md"

    if not template_path.exists():
        print(f"Error: {template_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    packages = []
    for item in repo_root.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            pkg_info = parse_pkgbuild(item)
            if pkg_info:
                packages.append(pkg_info)

    pkg_names = [p["name"] for p in packages]
    aur_info = fetch_aur_info(pkg_names)

    table_md = generate_markdown_table(packages, aur_info)

    template_content = template_path.read_text(encoding="utf-8")
    start_tag = "<!-- PACKAGES_TABLE_START -->"
    end_tag = "<!-- PACKAGES_TABLE_END -->"

    pattern = f"({re.escape(start_tag)}).*?({re.escape(end_tag)})"
    replacement = f"\\1\n{table_md}\n\\2"

    new_readme = re.sub(pattern, replacement, template_content, flags=re.DOTALL)

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Successfully updated {readme_path}")


if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    update_readme(repo_root)
