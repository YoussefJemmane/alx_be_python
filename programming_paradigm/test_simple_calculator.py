
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Test negative result
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative result
        self.assertEqual(self.calc.subtract(2, 5), -3)
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        # Test subtracting negative number
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test two negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        # Test division resulting in decimal
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        # Test two negative numbers
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()