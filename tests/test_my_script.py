import unittest
from src.main import add
from src.mysql_class import add
from mysql_class import MySQL

class TestMyScript(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

