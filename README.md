# Dune Prime

Dune Prime is a portable native engine for Cryo's **Dune** (1992, CD v3.7).
Players supply their own game files. No original game data or mods are included.

## Downloads

Get the current Windows, macOS and Linux applications from
[GitHub Releases](https://github.com/krismort/dune-prime/releases/latest).

- macOS: universal DMG for Apple silicon and Intel; drag Dune Prime to Applications.
- Windows x64: per-user installer or portable ZIP.
- Linux x86_64 and arm64: extract the tarball and run `./dune-prime`; optional `install.sh` adds the application menu entry.

Linux packages require glibc 2.36 or newer and SDL2. On Debian/Ubuntu,
`sudo apt install libsdl2-2.0-0` installs the runtime dependency.
The macOS application is ad-hoc signed, not notarized; Windows packages are unsigned.
Each release includes `SHA256SUMS` for its downloadable assets.

## Original game files

Supply `DUNE.DAT` and `DNCDPRG.EXE` from your own Dune CD version 3.7.
The first-run launcher and included `DUNECD/COPY-GAME-HERE.md` show where to put them.
Game data, CD images, extracted assets, saves and mod packages never belong in engine releases.

## re:cade storefront

The versionless [recade.game.json](recade.game.json) defines the store listing: title,
description, platforms, credits, controls, licence and original-CD requirements.
Read it from the release's resolved tagged commit, rather than from a moving branch.

A compatible release attaches **recade-release.tar.gz**. It contains the v1 recade.json
manifest, Windows x64 ZIP, universal macOS DMG, Linux x64 and arm64 archives, and a clean
launcher screenshot with alt text. The root descriptor stays outside that bundle.
The first screenshot can supply re:cade's cover and gallery image.

The existing manual re:cade importer can consume the exact tag. The automatic metadata
reader/updater is specified but is not enabled by creating these files.

## Repository and source policy

This public repository holds release metadata only. Engine development and builds stay
in a separate private repository. Engine source archives are not published here.
GitHub's automatic source ZIP/tar links contain only this repository's metadata.
Previously published engine source downloads have been withdrawn.

The engine is MIT licensed; see [LICENSE](LICENSE). Third-party components retain their
own licences, shipped with the applications. The original Dune game belongs to its owners.
