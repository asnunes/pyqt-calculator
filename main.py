import sys
from  ui.calculator import CalculatorUI
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec())
