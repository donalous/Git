import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_1(self):
        calc = Calculator(4, 0)
        result = calc.div()
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()