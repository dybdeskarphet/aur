# AUR Monorepo

<p align="left">
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/nvchecker.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/nvchecker.yml?branch=main&label=Update%20check&style=flat&logo=github" alt="nvchecker status"></a>
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/aur-deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/aur-deploy.yml?branch=main&label=AUR%20deploy&style=flat&logo=github" alt="aur-deploy status"></a>
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/release-builds.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/release-builds.yml?branch=main&label=Repo%20deploy&style=flat&logo=github" alt="aur-deploy status"></a>
</p>

Collection of AUR packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
| Package | Description | Repo Version | AUR Version | Status |
| :--- | :--- | :--- | :--- | :---: |
| [**antigravity-cli**](packages/antigravity-cli) | Google's agentic development platform (CLI companion) | `1.1.19_4894004681244672-1` | `Repo Only` | ![Repo Only](assets/dash-16.svg "Repo Only") |
| [**deskreen-ce-bin**](https://aur.archlinux.org/packages/deskreen-ce-bin) | Turn any device into a secondary screen for your computer - Community Edition (binary release) | `3.2.16-1` | `3.2.16-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**gams**](https://aur.archlinux.org/packages/gams) | A high-level modeling system for mathematical optimization | `54.3.1-1` | `54.3.0-1` | ![Ahead of AUR](assets/arrow-up-16.svg "Ahead of AUR") |
| [**gtkcsslanguageserver-git**](https://aur.archlinux.org/packages/gtkcsslanguageserver-git) | Language server for the GTK CSS flavor | `0.1.0.r111.gdcbe750-1` | `0.1.0.r111.gdcbe750-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**niri-companion**](https://aur.archlinux.org/packages/niri-companion) | Niri companion scripts: config generation, IPC extensions, workspace management | `5.0.0-1` | `5.0.0-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
| [**ungoogled-chromium-widevine-bin**](https://aur.archlinux.org/packages/ungoogled-chromium-widevine-bin) | A lightweight approach to removing Google web service dependency (with Widevine) | `151.0.7922.169-1` | `151.0.7922.169-1` | ![In sync with AUR](assets/check-16.svg "In sync with AUR") |
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- Updates monitored daily via `nvchecker`.
- Build tests before every version bump.
- Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).

## Using this GitHub repo as a Pacman package repository

See [releases](https://github.com/dybdeskarphet/aur/releases/tag/packages).
