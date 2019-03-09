from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel
from modules.display import Display
from modules.operations import OperationHandler

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
        operationSimbol = clickedButton.text()
        displayLabel = self.uic.findChild(QLabel, 'display')
        displayText = displayLabel.text()
        
        if Display.isNaN(displayText):
            self.toggleDisplayStyleSheet(True)
            return

        self.toggleDisplayStyleSheet(False)
        self.setNewOperation(displayText, operationSimbol)
        displayLabel.setText('')

    def resultButtonOnClick(self):
        displayLabel = self.uic.findChild(QLabel, 'display')
        displayText = displayLabel.text()
        nextNumber = float(displayLabel.text()) if displayText is not '' else 0.0
        result = self.operationHandler.operate(nextNumber)
        displayLabel.setText(str(result))

    def delButtonOnClick(self):
        self.delDisplayChar()

    def clearButtonOnClick(self):
        self.resetDisplayText()

    def setDisplay(self, input):
        displayLabel = self.uic.findChild(QLabel, 'display')
        currentText = displayLabel.text()
        output = Display.inputHandler(currentText, input)
        displayLabel.setText(output)
        self.toggleDisplayStyleSheet(False)

    def delDisplayChar(self):
        displayLabel = self.uic.findChild(QLabel, 'display')
        currentText = displayLabel.text()
        output = Display.delHandler(currentText)
        displayLabel.setText(output)

    def toggleDisplayStyleSheet(self, isError):
        displayLabel = self.uic.findChild(QLabel, 'display')
        color = 'red' if isError else 'black'
        displayLabel.setStyleSheet('color: ' + color)

    def resetDisplayText(self):
        displayLabel = self.uic.findChild(QLabel, 'display')
        displayLabel.setText('0')
        self.toggleDisplayStyleSheet(False)

    def setNewOperation(self, displayText, operationSimbol):
        mapper = {'/': OperationHandler.DIVIDE_OP, '*': OperationHandler.MULTIPLY_OP, 
        '+': OperationHandler.ADD_OP, '-': OperationHandler.SUBTRACT_OP}

        prevNumber = float(displayText) if displayText is not '' else 0.0
        self.operationHandler.setNewOperation(prevNumber, mapper[operationSimbol])
