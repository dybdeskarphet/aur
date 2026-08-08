# AUR Packages Monorepo

Collection of Arch Linux User Repository (AUR) packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
| Package | Description | Repo Version | AUR Version | Status |
| :--- | :--- | :--- | :--- | :--- |
| [**gams**](https://aur.archlinux.org/packages/gams) | A high-level modeling system for mathematical optimization | `54.2.0-1` | `54.2.0-1` | 🟢 Synced |
| [**niri-companion**](https://aur.archlinux.org/packages/niri-companion) | Niri companion scripts: config generation, IPC extensions, workspace management | `5.0.0-1` | `5.0.0-1` | 🟢 Synced |
| [**ungoogled-chromium-widevine-bin**](https://aur.archlinux.org/packages/ungoogled-chromium-widevine-bin) | A lightweight approach to removing Google web service dependency (with Widevine) | `150.0.7871.186-1` | `150.0.7871.186-1` | 🟢 Synced |
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- **Upstream Release Tracking**: Monitored daily via `nvchecker`.
- **Build Verification**: Every version bump is verified using `makepkg` inside an `archlinux:latest` container before committing.
- **AUR Deployment**: Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).
