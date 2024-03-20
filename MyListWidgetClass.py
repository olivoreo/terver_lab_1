from PyQt6 import QtWidgets, QtCore
from NaturalNumberValidator import setValidator
from myQTFunctions import getIntFromLineEdit
class MyListWidgetClass:
    def __init__(self, centralwidget):
        self.scrollArea = QtWidgets.QScrollArea(parent=centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 372, 106))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayoutForScroll = QtWidgets.QFormLayout()
        self.formLayoutForScroll.setContentsMargins(10, 10, 10, 10)
        self.formLayoutForScroll.setSpacing(7)
        self.formLayoutForScroll.setObjectName("formLayoutForScroll")

        self.scrollAreaWidgetContents.setLayout(self.formLayoutForScroll)

    labelList = []
    lineEditList = []
    nameElement = ""

    def setNumOfListElements(self, num):

        mListLength = len(self.lineEditList)
        for i in range(num - mListLength):
            self.addListElement()
        for i in range(mListLength-1, num-1, -1):
            self.lineEditList[i].deleteLater()
            self.labelList[i].deleteLater()
            self.formLayoutForScroll.removeRow(i)
            self.labelList.pop()
            self.lineEditList.pop()
    def addListElement(self):
        index = len(self.lineEditList)

        label = QtWidgets.QLabel(parent=self.scrollArea)
        label.setText(self.nameElement+str(index)+":")

        lineEdit = QtWidgets.QLineEdit(parent=self.scrollArea)
        setValidator(lineEdit)

        self.labelList.append(label)
        self.lineEditList.append(lineEdit)

        self.formLayoutForScroll.setWidget(index, QtWidgets.QFormLayout.ItemRole.LabelRole, label)
        self.formLayoutForScroll.setWidget(index, QtWidgets.QFormLayout.ItemRole.FieldRole, lineEdit)
    def getList(self):
        numList = []
        for lineEdit in self.lineEditList:
            numList.append(getIntFromLineEdit(lineEdit))
        return numList
