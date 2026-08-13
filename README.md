# AUR Packages Monorepo

<p align="left">
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/nvchecker.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/nvchecker.yml?branch=main&label=nvchecker%20check&style=flat-square&logo=github" alt="nvchecker status"></a>
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/aur-deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/aur-deploy.yml?branch=main&label=AUR%20deploy&style=flat-square&logo=github" alt="aur-deploy status"></a>
</p>

Collection of Arch Linux User Repository (AUR) packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
| Package | Description | Repo Version | AUR Version | Status |
| :--- | :--- | :--- | :--- | :---: |
| [**deskreen-ce-bin**](https://aur.archlinux.org/packages/deskreen-ce-bin) | Turn any device into a secondary screen for your computer - Community Edition (binary release) | `3.2.16-1` | `3.2.16-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**gams**](https://aur.archlinux.org/packages/gams) | A high-level modeling system for mathematical optimization | `54.2.2-1` | `54.2.2-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**gtkcsslanguageserver-git**](https://aur.archlinux.org/packages/gtkcsslanguageserver-git) | Language server for the GTK CSS flavor | `0.1.0.r111.gdcbe750-1` | `0.1.0.r111.gdcbe750-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**niri-companion**](https://aur.archlinux.org/packages/niri-companion) | Niri companion scripts: config generation, IPC extensions, workspace management | `5.0.0-1` | `5.0.0-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**ungoogled-chromium-widevine-bin**](https://aur.archlinux.org/packages/ungoogled-chromium-widevine-bin) | A lightweight approach to removing Google web service dependency (with Widevine) | `151.0.7922.108-1` | `151.0.7922.108-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- **Upstream Release Tracking**: Monitored daily via `nvchecker`.
- **Build Verification**: Every version bump is verified using `makepkg` inside an `archlinux:latest` container before committing.
- **AUR Deployment**: Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).
