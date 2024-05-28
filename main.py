## Импортируем библиотеку для создания графического интерфейса
from PyQt5 import QtCore, QtGui, QtWidgets

##  Класс для реализации калькулятора
class Calculator(QtWidgets.QWidget):
    """
    Простой калькулятор с графическим интерфейсом на PyQt5.

    :param label: Поле для отображения ввода и результата.
    :type label: QtWidgets.QLabel
    """
    def __init__(self):
        """
        Инициализирует калькулятор и создает его интерфейс.
        """
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.label = QtWidgets.QLabel("0", self)
        self.label.setGeometry(20, 20, 260, 50)
        self.label.setStyleSheet("border: 1px solid gray; font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.create_buttons()

    def create_buttons(self):
        """
        Создает кнопки калькулятора и размещает их на интерфейсе.
        """
        button_list = [
            'C', '', '⌫', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '00', '0', '.', '='
        ]

        row = 1
        col = 0
        for button_text in button_list:
            button = QtWidgets.QPushButton(button_text, self)
            button.setGeometry(20 + col * 70, 80 + row * 60, 60, 50)
            button.clicked.connect(self.button_clicked)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_clicked(self):
        """
        Обрабатывает нажатия на кнопки калькулятора.
        """
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.label.text()))
                self.label.setText(result)
            except:
                self.label.setText("Ошибка")
        elif text == 'C':
            self.label.setText("0")
        elif text == '⌫':
            self.label.setText(self.label.text()[:-1])
        else:
            if self.label.text() == "0":
                self.label.setText(text)
            else:
                self.label.setText(self.label.text() + text)

##  Создание приложения и запуск калькулятора
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
