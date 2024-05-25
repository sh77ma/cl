def sum(a, b):
  """Суммирует два числа."""
  return a + b

def subtract(a, b):
  """Вычитает из первого числа второе."""
  return a - b

def multiply(a, b):
  """Перемножает два числа."""
  return a * b

def divide(a, b):
  """Делит первое число на второе."""
  if b == 0:
    return "Деление на ноль невозможно"
  else:
    return a / b

while True:
  print("Выберите операцию:")
  print("1. Сложение")
  print("2. Вычитание")
  print("3. Умножение")
  print("4. Деление")
  print("5. Выход")

  choice = input("Введите номер операции: ")

  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Введите первое число: "))
      num2 = float(input("Введите второе число: "))
    except ValueError:
      print("Некорректный ввод. Пожалуйста, введите числа.")
      continue

    if choice == '1':
      print(num1, "+", num2, "=", sum(num1, num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

  elif choice == '5':
    break
  else:
    print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")
