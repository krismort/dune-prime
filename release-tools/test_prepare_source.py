import hashlib, importlib.util, io
from pathlib import Path
import tarfile, tempfile, unittest
SCRIPT=Path(__file__).with_name('prepare-source.py')
class PrepareSourceTest(unittest.TestCase):
 def archive(self, name='src/example.c', link=False):
  out=io.BytesIO()
  with tarfile.open(fileobj=out,mode='w:gz') as tar:
   for path,data in [('VERSION',b'0.1.0\n'),(name,b'int example;\n')]:
    item=tarfile.TarInfo('DunePrime-0.1.0-source/'+path);item.size=len(data)
    if link and path==name:item.type=tarfile.SYMTYPE;item.linkname='/private';item.size=0
    tar.addfile(item,io.BytesIO(data) if item.isfile() else None)
  return out.getvalue()
 def module(self):
  self.assertTrue(SCRIPT.exists(),'Verified source preparation helper is missing')
  spec=importlib.util.spec_from_file_location('prepare',SCRIPT);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
 def test_valid_source_is_extracted_exactly(self):
  m=self.module();data=self.archive()
  with tempfile.TemporaryDirectory() as tmp:
   dest=Path(tmp)/'source';m.extract_source(data,hashlib.sha256(data).hexdigest(),'0.1.0',dest)
   self.assertEqual((dest/'src/example.c').read_bytes(),b'int example;\n')
 def test_checksum_failure_writes_no_source(self):
  m=self.module();data=self.archive()
  with tempfile.TemporaryDirectory() as tmp:
   dest=Path(tmp)/'source'
   with self.assertRaises(ValueError):m.extract_source(data,'0'*64,'0.1.0',dest)
   self.assertFalse(dest.exists())
 def test_mod_game_traversal_and_links_are_rejected(self):
  m=self.module()
  for name,link in [('mods/x/manifest.json',False),('DUNECD/DUNE.DAT',False),('../escape.c',False),('src/example.c',True)]:
   with self.subTest(name=name,link=link),tempfile.TemporaryDirectory() as tmp:
    data=self.archive(name,link);dest=Path(tmp)/'source'
    with self.assertRaises(ValueError):m.extract_source(data,hashlib.sha256(data).hexdigest(),'0.1.0',dest)
    self.assertFalse(dest.exists())
if __name__=='__main__':unittest.main()
