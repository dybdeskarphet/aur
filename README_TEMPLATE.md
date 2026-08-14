# AUR Monorepo

<p align="left">
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/nvchecker.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/nvchecker.yml?branch=main&label=nvchecker%20check&style=flat-square&logo=github" alt="nvchecker status"></a>
  <a href="https://github.com/dybdeskarphet/aur/actions/workflows/aur-deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/dybdeskarphet/aur/aur-deploy.yml?branch=main&label=AUR%20deploy&style=flat-square&logo=github" alt="aur-deploy status"></a>
</p>

Collection of AUR packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- Updates monitored daily via `nvchecker`.
- Build tests before every version bump.
- Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).

## Using this GitHub repo as a Pacman package repository

See [releases](https://github.com/dybdeskarphet/aur/releases/tag/packages).
