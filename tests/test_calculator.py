import unittest
import math

from calculator import evaluate

class TestCalculator(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(evaluate('1 + 2'), 3)
        self.assertEqual(evaluate('2 * 3'), 6)
        self.assertEqual(evaluate('10 / 2'), 5)
        self.assertEqual(evaluate('2 ** 3'), 8)

    def test_math_functions(self):
        self.assertAlmostEqual(evaluate('sin(pi / 2)'), 1.0)
        self.assertAlmostEqual(evaluate('log(e)'), 1.0)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            evaluate('import os')

if __name__ == '__main__':
    unittest.main()
