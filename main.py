import sys
from PySide6.QtWidgets import QApplication
from src.calculadora import CalculatorWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
