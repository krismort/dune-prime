# Dune Prime

Dune Prime is a portable, MIT-licensed engine for Cryo's **Dune** (1992, CD version 3.7).
Players supply their own game files; the engine includes no original game data.

## Downloads

Download published releases from [GitHub Releases](https://github.com/krismort/dune-prime/releases).
The initial release provides the engine source archive and its SHA-256 checksum.
Application builds will be listed as separate assets when available.

Use the attached `DunePrime-<version>-source.tar.gz` asset for the engine source.
GitHub's automatic **Source code** ZIP/tar downloads contain this release repository's
metadata and documentation, rather than the engine.

## Build from released source

Extract the engine source asset. Install a C/C++ compiler, make, pkg-config and SDL2
development files, then run `make` inside the extracted folder. Its README contains
platform build and test instructions. No game data or mods are needed to compile.

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
