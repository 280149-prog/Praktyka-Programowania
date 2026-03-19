import unittest
from main import add

class add_test(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(add(""),0)

    def test_one_input(self):
        self.assertEqual(add("1"),1)

    def test_two_input(self):
        self.assertEqual(add("1,2"),3)

    def test_many_input(self):
        self.assertEqual(add("1,2,3,4"),10)

    def test_output_err(self):
        with self.assertRaises(ValueError):
            add(".")

    def test_enter_input(self):
        self.assertEqual(add("1\n2,3"),6)

