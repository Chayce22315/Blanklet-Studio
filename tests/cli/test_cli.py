import io
import sys
import unittest
from cli import blanklet

class TestCLI(unittest.TestCase):
    def test_help(self):
        out = io.StringIO()
        old = sys.stdout
        sys.stdout = out
        rc = blanklet.main([])
        sys.stdout = old
        self.assertEqual(rc, 0)
        self.assertIn('Available commands', out.getvalue())

    def test_build(self):
        rc = blanklet.main(['build','--target','web'])
        self.assertEqual(rc, 0)

if __name__ == '__main__':
    unittest.main()
