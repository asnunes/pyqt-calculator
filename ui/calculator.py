from PyQt5 import QtWidgets, uic

class CalculatorUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(CalculatorUI, self).__init__()
        self.uic = uic.loadUi('ui/calculator.ui', self)

    def numberButtonOnClick(self):
        print("button clicked")