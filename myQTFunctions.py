from PyQt6.QtGui import QValidator
from PyQt6 import QtCore, QtGui, QtWidgets
def getIntFromLineEdit(lineEdit):
    text = lineEdit.text()
    validator_state = lineEdit.validator().validate(text, 0)[0]
    if (text == ""):
        return 0
    elif (validator_state == QValidator.State.Acceptable):
        return int(text)
    return 0