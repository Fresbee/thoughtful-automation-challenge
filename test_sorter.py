import unittest
from sorter import sort

class TestSorter(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")
        self.assertEqual(sort(500, 40, 30, 10), "STANDARD")
        self.assertEqual(sort(100, 100, 99.9, 19.9), "STANDARD")

    def test_special_package_bulky(self):
        self.assertEqual(sort(2000, 400, 300, 19.9), "SPECIAL")
        self.assertEqual(sort(1000, 1, 1, 19.9), "SPECIAL")
        self.assertEqual(sort(1, 1000, 1, 19.9), "SPECIAL")
        self.assertEqual(sort(1, 1, 1000, 19.9), "SPECIAL")

    def test_special_package_heavy(self):
        self.assertEqual(sort(100, 100, 99.9, 20), "SPECIAL")

    def test_rejected_package(self):
        self.assertEqual(sort(1000, 400, 300, 20), "REJECTED")
        self.assertEqual(sort(400, 1000, 300, 20), "REJECTED")
        self.assertEqual(sort(400, 400, 1000, 20), "REJECTED")
        self.assertEqual(sort(1000, 1000, 1, 20), "REJECTED")
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, -1)
        with self.assertRaises(ValueError):
            sort(0, 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 0, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 0, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, 0)
