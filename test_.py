import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_1(self):
        # Arrange
        calc = Calculator(3, 5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 8, "Addition failed")

    def test_2(self):
        # Arrange
        calc = Calculator(-3, 5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 2, "Addition of negative numbers failed")

    def test_3(self):
        # Arrange
        calc = Calculator(3.5, 2.5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 6.0, "Addition of float numbers failed")

    def test_4(self):
        # Arrange
        calc = Calculator(0, 0)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 0, "Addition of zero failed")

if __name__ == '__main__':
    unittest.main()