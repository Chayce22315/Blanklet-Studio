import os
import unittest
from cli import blanklet

class TestCLIExtra(unittest.TestCase):
    def test_tui(self):
        rc = blanklet.main(['tui'])
        self.assertEqual(rc, 0)

    def test_pack_output(self):
        outname = 'tests_tmp.pack'
        try:
            rc = blanklet.main(['pack','--output', outname])
            self.assertEqual(rc, 0)
            self.assertTrue(os.path.exists(outname))
            with open(outname,'rb') as f:
                data = f.read()
            self.assertIn(b'BLANKLET_PACK_v1', data)
        finally:
            if os.path.exists(outname): os.remove(outname)

if __name__ == '__main__':
    unittest.main()
