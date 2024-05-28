import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def setUp(self):
        clear()

    def test_addition(self):
        ui.label.setText("2")
        add()
        ui.label.setText("3")
        equal()
        self.assertEqual(ui.label.text(), "5.0")

    def test_subtraction(self):
        ui.label.setText("5")
        subtract()
        ui.label.setText("2")
        equal()
        self.assertEqual(ui.label.text(), "3.0")

    def test_multiplication(self):
        ui.label.setText("2")
        multiply()
        ui.label.setText("3")
        equal()
        self.assertEqual(ui.label.text(), "6.0")

    def test_division(self):
        ui.label.setText("6")
        divide()
        ui.label.setText("2")
        equal()
        self.assertEqual(ui.label.text(), "3.0")

    def test_clear(self):
        ui.label.setText("123")
        clear()
        self.assertEqual(ui.label.text(), "0")

if __name__ == "__main__":
    unittest.main()
