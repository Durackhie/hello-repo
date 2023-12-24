from mypythonproject
import unittest

class TestScriptFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
