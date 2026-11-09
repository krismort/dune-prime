from pathlib import Path, PurePosixPath
import os, sys, tarfile, zipfile

HASH = os.environ['DUNE_PRIME_BUILD_HASH']
VERSION = os.environ['RELEASE_VERSION']
FORBIDDEN_DIRS = {'mods','tools-mod','assets_override','dump','captures','extracted','exports','__pycache__','.git'}
FORBIDDEN_EXT = {'.dat','.com','.hsq','.hnm','.voc','.sav','.drv','.iso','.bin','.wav','.mp3','.ogg','.flac','.ppm','.tga','.zip','.7z','.rar'}

def check(name, read):
    parts=PurePosixPath(name).parts
    low=[p.lower() for p in parts]
    suffix=PurePosixPath(name).suffix.lower()
    assert '..' not in parts and not name.startswith('/'), name
    assert not any(p in FORBIDDEN_DIRS or p.startswith('._') or p=='.ds_store' for p in low), name
    assert suffix not in FORBIDDEN_EXT, name
    assert low[-1]!='manifest.json', name
    if 'dunecd' in low:
        assert low[-1]=='copy-game-here.md', name
    if suffix=='.exe':
        assert low[-1] in {'dune-prime.exe','uninstall.exe'},name
    if suffix=='.png':
        assert low[-1]=='dune-prime.png',name
    if suffix=='.bmp':
        assert '$pluginsdir' in low,name
    if low[-1]=='build-info.txt':
        data=read().decode()
        assert f'Dune Prime {VERSION}\n' in data and f'build {HASH}\n' in data and '-dirty' not in data,name
        return True
    return False

def audit(path):
    count=info=0
    if path.is_dir():
        for base,dirs,files in os.walk(path,followlinks=False):
            for name in dirs+files:
                p=Path(base)/name
                if p.is_symlink():
                    if p.name=='Applications' and p.parent==path:
                        assert os.readlink(p)=='/Applications'
                    else:
                        assert p.resolve().is_relative_to(path.resolve()),p
            for name in files:
                p=Path(base)/name
                if p.is_symlink():continue
                info+=check(p.relative_to(path).as_posix(),p.read_bytes);count+=1
    elif zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            for item in z.infolist():
                if item.is_dir():continue
                assert (item.external_attr>>16)&0o170000 != 0o120000,item.filename
                info+=check(item.filename,lambda item=item:z.read(item));count+=1
    else:
        with tarfile.open(path) as tar:
            for item in tar:
                if item.isdir():continue
                assert item.isfile(),item.name
                info+=check(item.name,lambda item=item:tar.extractfile(item).read());count+=1
    assert info==1,(path,info)
    print(f'PASS: {path.name}: {count} files; expected release build; no game data, mod packages, saves or captures')

if __name__=='__main__':
    for arg in sys.argv[1:]:audit(Path(arg))
