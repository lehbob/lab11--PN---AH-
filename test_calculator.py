# https://github.com/lehbob/lab11--PN---AH-.git
# Partner 1: Phuc Nguyen
# Partner 2: Aydan Haynes

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(2, 5), -3)
        self.assertEqual(sub(0, 0), 0)
    ##########################

    ######## Partner 1
    # Partner 1 handles multiply, divide, etc.
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(16, 4), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(5, 1)
    ##########################

    ######## Partner 1
    # Partner 1 handles log_invalid_argument, hypotenuse, sqrt, etc.
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
