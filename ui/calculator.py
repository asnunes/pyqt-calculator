from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel
from models.display import Display
from models.operations import OperationHandler

class CalculatorUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(CalculatorUI, self).__init__()
        self.uic = uic.loadUi('ui/calculator.ui', self)
        self.operationHandler = OperationHandler()

    def numberButtonOnClick(self):
        clickedButton = self.sender()
        number = int(clickedButton.text())
        self.setDisplay(number)

    def dotButtonOnClick(self):
        self.setDisplay('.')

    def operationButtonOnClick(self):
        clickedButton = self.sender()
        displayLabel = self.uic.findChild(QLabel, 'display')
        prevNumber = float(displayLabel.text())
        mapper = {'/': OperationHandler.DIVIDE_OP, '*': OperationHandler.MULTIPLY_OP, 
        '+': OperationHandler.ADD_OP, '-': OperationHandler.SUBTRACT_OP}

        self.operationHandler.setNewOperation(prevNumber, mapper[clickedButton.text()])
        displayLabel.setText('')

    def resultButtonOnClick(self):
        displayLabel = self.uic.findChild(QLabel, 'display')
        nextNumber = float(displayLabel.text())
        result = self.operationHandler.operate(nextNumber)
        displayLabel.setText(str(result))

    def delButtonOnClick(self):
        self.delDisplayChar()

    def setDisplay(self, input):
        displayLabel = self.uic.findChild(QLabel, 'display')
        currentText = displayLabel.text()
        output = Display.inputHandler(currentText, input)
        displayLabel.setText(output)

    def delDisplayChar(self):
        displayLabel = self.uic.findChild(QLabel, 'display')
        currentText = displayLabel.text()
        output = currentText[:-1]
        displayLabel.setText(output)