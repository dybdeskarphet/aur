# AUR Packages Monorepo

Collection of Arch Linux User Repository (AUR) packages maintained by me.

## Packages Overview

<!-- PACKAGES_TABLE_START -->
<!-- PACKAGES_TABLE_END -->

## Automation & Workflow

- **Upstream Release Tracking**: Monitored daily via `nvchecker`.
- **Build Verification**: Every version bump is verified using `makepkg` inside an `archlinux:latest` container before committing.
- **AUR Deployment**: Pushes to `main` automatically deploy to respective AUR repositories (`ssh://aur.archlinux.org/$pkg.git`).
