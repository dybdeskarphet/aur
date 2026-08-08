# AUR Packages Monorepo

<p align="left">
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/nvchecker.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/nvchecker.yml?branch=main&label=nvchecker%20check&style=flat-square&logo=github" alt="nvchecker status"></a>
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/aur-deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/aur-deploy.yml?branch=main&label=AUR%20deploy&style=flat-square&logo=github" alt="aur-deploy status"></a>
</p>

Collection of Arch Linux User Repository (AUR) packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- **Upstream Release Tracking**: Monitored daily via `nvchecker`.
- **Build Verification**: Every version bump is verified using `makepkg` inside an `archlinux:latest` container before committing.
- **AUR Deployment**: Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).
