# Dune Prime

Dune Prime is a portable, MIT-licensed engine for Cryo's **Dune** (1992, CD version 3.7).
Players supply their own game files; the engine includes no original game data.

## Downloads

Download published releases from [GitHub Releases](https://github.com/krismort/dune-prime/releases).

| Platform | Download | Start |
|---|---|---|
| macOS 11+, Apple silicon and Intel | [Universal DMG](https://github.com/krismort/dune-prime/releases/download/v0.1.0/DunePrime-0.1.0%2B22ea583b8-macos-universal.dmg) | Open the DMG and drag Dune Prime to Applications |
| Windows 10+, x64 | [Installer](https://github.com/krismort/dune-prime/releases/download/v0.1.0/DunePrime-0.1.0%2B22ea583b8-windows-x64-setup.exe) or [portable ZIP](https://github.com/krismort/dune-prime/releases/download/v0.1.0/DunePrime-0.1.0%2B22ea583b8-windows-x64.zip) | Install per user, or extract the ZIP and run dune-prime.exe |
| Linux x86_64 | [tar.gz](https://github.com/krismort/dune-prime/releases/download/v0.1.0/DunePrime-0.1.0%2B22ea583b8-linux-x86_64.tar.gz) | Extract, install SDL2, run ./dune-prime |
| Linux arm64 | [tar.gz](https://github.com/krismort/dune-prime/releases/download/v0.1.0/DunePrime-0.1.0%2B22ea583b8-linux-arm64.tar.gz) | Extract, install SDL2, run ./dune-prime |

Linux packages target glibc 2.36 or newer. On Debian/Ubuntu, install SDL2 with
`sudo apt install libsdl2-2.0-0`. Each Linux package includes an optional `install.sh`.
The macOS app is ad-hoc signed and not notarized; Windows packages are unsigned.

[SHA-256 checksums](https://github.com/krismort/dune-prime/releases/download/v0.1.0/SHA256SUMS) cover all release downloads. Engine source and its checksum are also attached.

Use the attached `DunePrime-<version>-source.tar.gz` asset for the engine source.
GitHub's automatic **Source code** ZIP/tar downloads contain this release repository's
metadata and documentation, rather than the engine.

## Build from released source

Extract the engine source asset. Install a C/C++ compiler, make, pkg-config and SDL2
development files, then run `make` inside the extracted folder. Its README contains
platform build and test instructions. No game data or mods are needed to compile.
For GCC, this initial snapshot requires the standard algorithm header explicitly
available: `make CXX='g++ -include algorithm'`. The release workflow applies that
compiler setting without modifying the tagged source.

To play, supply `DUNE.DAT` and `DNCDPRG.EXE` from your own Dune CD version 3.7 as
explained in the archive's `DUNECD/COPY-GAME-HERE.md`. Keep these files on your own machine.

## Repository scope

This public repository contains release documentation, version metadata and GitHub
Releases. Development happens separately. Only reviewed, versioned engine source
snapshots and application packages are published here as release assets.

Mods are independently maintained and installed. No mod packages, original game files,
extracted game assets, captured fixtures or saved games are included in engine releases.

## Licence

The Dune Prime engine is MIT licensed; see [LICENSE](LICENSE). Bundled third-party
source retains its own licences, included in the engine source archive. Dune and its
original game data belong to their respective owners and are not part of this project.
