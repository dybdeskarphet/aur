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

    pkgver_match = re.search(r"^pkgver=([^\s#]+)", content, re.MULTILINE)
    pkgrel_match = re.search(r"^pkgrel=([^\s#]+)", content, re.MULTILINE)
    epoch_match = re.search(r"^epoch=([^\s#]+)", content, re.MULTILINE)
    desc_match = re.search(r"^pkgdesc=['\"](.+)['\"]$", content, re.MULTILINE) or re.search(
        r"^pkgdesc=([^\n#]+)", content, re.MULTILINE
    )

    pkgver = pkgver_match.group(1).strip("'\"") if pkgver_match else "unknown"
    pkgrel = pkgrel_match.group(1).strip("'\"") if pkgrel_match else "1"
    epoch = epoch_match.group(1).strip("'\"") if epoch_match else ""
    desc = desc_match.group(1).strip("'\"") if desc_match else ""

    ver_str = f"{epoch}:{pkgver}-{pkgrel}" if epoch else f"{pkgver}-{pkgrel}"

    noaur = (pkg_dir / ".noaur").exists()

    return {
        "name": pkg_dir.name,
        "repo_ver": ver_str,
        "desc": desc,
        "noaur": noaur,
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


def compare_versions(v1: str, v2: str) -> int:
    """Pure Python Arch Linux version comparator (epoch:pkgver-pkgrel).
    Returns 1 if v1 > v2, -1 if v1 < v2, 0 if v1 == v2.
    """
    if v1 == v2:
        return 0

    def parse_ver(v_str: str):
        epoch = 0
        if ":" in v_str:
            epoch_str, v_str = v_str.split(":", 1)
            epoch = int(epoch_str) if epoch_str.isdigit() else 0

        pkgrel = "1"
        if "-" in v_str:
            v_str, pkgrel = v_str.rsplit("-", 1)

        def tokenize(s: str):
            tokens = []
            for part in re.split(r"([0-9]+|[^0-9._~-]+)", s):
                if not part or part in "._~-":
                    continue
                if part.isdigit():
                    tokens.append((1, int(part)))
                else:
                    tokens.append((0, part))
            return tokens

        return (epoch, tokenize(v_str), tokenize(pkgrel))

    v1_t = parse_ver(v1)
    v2_t = parse_ver(v2)

    if v1_t > v2_t:
        return 1
    elif v1_t < v2_t:
        return -1
    return 0


def generate_markdown_table(packages: list[dict], aur_info: dict[str, str]) -> str:
    lines = [
        "| Package | Description | Repo Version | AUR Version | Status |",
        "| :--- | :--- | :--- | :--- | :---: |",
    ]

    for pkg in sorted(packages, key=lambda x: x["name"]):
        name = pkg["name"]
        repo_ver = pkg["repo_ver"]
        desc = pkg["desc"]

        if pkg.get("noaur"):
            aur_ver = "Repo Only"
            status_badge = '![Repo Only](assets/dash-16.svg "Repo Only")'
            pkg_link = f"packages/{name}"
            lines.append(
                f"| [**{name}**]({pkg_link}) | {desc} | `{repo_ver}` | `{aur_ver}` | {status_badge} |"
            )
            continue

        aur_ver = aur_info.get(name, "Not Published")

        if aur_ver == "Not Published":
            status_badge = '![Not published](assets/dash-16.svg "Not published")'
        else:
            cmp_res = compare_versions(repo_ver, aur_ver)
            if cmp_res == 0:
                status_badge = '![In sync with AUR](assets/check-16.svg "In sync with AUR")'
            elif cmp_res > 0:
                status_badge = '![Ahead of AUR](assets/arrow-up-16.svg "Ahead of AUR")'
            else:
                status_badge = '![Out of date](assets/clock-16.svg "Out of date")'

        aur_link = f"https://aur.archlinux.org/packages/{name}"
        lines.append(
            f"| [**{name}**]({aur_link}) | {desc} | `{repo_ver}` | `{aur_ver}` | {status_badge} |"
        )

    return "\n".join(lines)


def update_readme(repo_root: Path):
    template_path = repo_root / "README_TEMPLATE.md"
    readme_path = repo_root / "README.md"

    if not template_path.exists():
        print(f"Error: {template_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    packages = []
    packages_dir = repo_root / "packages"
    if packages_dir.exists():
        for item in packages_dir.iterdir():
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
