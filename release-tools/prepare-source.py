"""Prepare a checksum-verified published engine snapshot for release builds."""
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tarfile
import urllib.request

BLOCKED = {'mods', 'tools-mod', 'assets_override', 'captures', 'dump', 'extracted',
           'exports', '__pycache__', '.git', 'superpowers'}
GAME_EXTENSIONS = {'.dat', '.exe', '.com', '.hsq', '.hnm', '.voc', '.sav', '.drv', '.iso', '.bin'}


def extract_source(data, expected_sha256, version, destination):
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise ValueError('Published source checksum does not match release metadata')
    prefix = f'DunePrime-{version}-source'
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        for member in archive:
            parts = PurePosixPath(member.name).parts
            if (not member.isfile() or len(parts) < 2 or parts[0] != prefix or
                    '..' in parts or any(p.lower() in BLOCKED for p in parts)):
                raise ValueError(f'Unsafe or non-source archive entry: {member.name}')
            relative = PurePosixPath(*parts[1:])
            lower = [p.lower() for p in relative.parts]
            if (relative.suffix.lower() in GAME_EXTENSIONS or lower[-1] == 'manifest.json' or
                    ('dunecd' in lower and relative.as_posix() != 'DUNECD/COPY-GAME-HERE.md')):
                raise ValueError(f'Game or mod payload in source archive: {member.name}')
            if relative in files:
                raise ValueError(f'Duplicate archive entry: {member.name}')
            files[relative] = archive.extractfile(member).read()
    if files.get(PurePosixPath('VERSION'), b'').decode().strip() != version:
        raise ValueError('Source VERSION differs from requested release')
    destination.mkdir(parents=True, exist_ok=False)
    for relative, content in files.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        target.chmod(0o755 if relative.suffix == '.sh' else 0o644)
    return len(files)


def main():
    version = os.environ['RELEASE_VERSION']
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Release version must be MAJOR.MINOR.PATCH')
    metadata = json.loads((Path(__file__).resolve().parents[1] / 'releases' / f'v{version}.json').read_text())
    commit = metadata['source']['commit']
    if metadata['version'] != version or not re.fullmatch(r'[a-f0-9]{40}', commit):
        raise ValueError('Invalid release metadata')
    name = f'DunePrime-{version}-source.tar.gz'
    asset = next(item for item in metadata['assets'] if item['name'] == name)
    url = f'https://github.com/krismort/dune-prime/releases/download/v{version}/{name}'
    request = urllib.request.Request(url, headers={'User-Agent': 'DunePrimeReleaseBuild'})
    with urllib.request.urlopen(request, timeout=120) as response:
        data = response.read()
    destination = Path(os.environ['RUNNER_TEMP']) / 'engine-source'
    count = extract_source(data, asset['sha256'], version, destination)
    with Path(os.environ['GITHUB_ENV']).open('a') as env:
        env.write(f'BUILD_SOURCE={destination}\nDUNE_PRIME_BUILD_HASH={commit[:9]}\nSOURCE_COMMIT={commit}\n')
    print(f'Prepared {count} verified source files from release commit {commit}')


if __name__ == '__main__':
    main()
