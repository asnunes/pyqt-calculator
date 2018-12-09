from PyQt5 import QtWidgets, uic

class Calculator(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Calculator, self).__init__()

        self.uic = uic.loadUi('ui/main.ui', self)