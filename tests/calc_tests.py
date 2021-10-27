import unittest
from modules.calculator import *

class TestCalc(unittest.TestCase):

    def test_add_both_positive(self):
        self.assertEqual(5, add(2,3))
    
    def test_add_one_negative(self):
        self.assertEqual(6, add(-2, 8))

    def test_substract(self):
        self.assertEqual(5, subtract(8, 3))

    def test_divide(self):
        self.assertEqual(2, divide(4, 2))

    def test_multiply(self):
        self.assertEqual(10, multiply(2, 5))
