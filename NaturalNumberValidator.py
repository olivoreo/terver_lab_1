from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

class NaturalNumberValidator(QRegularExpressionValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        reg_exp = QRegularExpression("[1-9]\\d*")  # Регулярное выражение для натуральных чисел
        self.setRegularExpression(reg_exp)


def setValidator(lineEdit):
    naturalValidator = NaturalNumberValidator()
    lineEdit.setValidator(naturalValidator)

# Пример использования:
# validator = NaturalNumberValidator()
# line_edit = QLineEdit()
# line_edit.setValidator(validator)
