from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel
from models.display import Display

class CalculatorUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(CalculatorUI, self).__init__()
        self.uic = uic.loadUi('ui/calculator.ui', self)

    def numberButtonOnClick(self):
        clicked_button = self.sender()
        number = int(clicked_button.text())
        self.setDisplay(number)

    def dotButtonOnClick(self):
        self.setDisplay('.')

    def setDisplay(self, input):
        displayLabel = self.uic.findChild(QLabel, 'display')
        currentText = displayLabel.text()
        output = Display.inputHandler(currentText, input)
        displayLabel.setText(output)