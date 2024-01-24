import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(self.calc.value, 0)

    def test_add_method(self):
        self.calc.add(1, 3)
        self.assertEqual(self.calc.value, 4)

    def test_subtract_method(self):
        self.calc.subtract(1, 3)
        self.assertEqual(self.calc.value, -2)
    
    def tearDown(self):
        del self.calc


if __name__ == '__main__':
    unittest.main()