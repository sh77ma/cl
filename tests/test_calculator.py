from src import calculator

def test_sum():
  assert calculator.sum(1, 2) == 3

def test_subtract():
  assert calculator.subtract(5, 3) == 2

def test_multiply():
  assert calculator.multiply(4, 2) == 8

def test_divide():
  assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
  assert calculator.divide(10, 0) == "Деление на ноль невозможно"
