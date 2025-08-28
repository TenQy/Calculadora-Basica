import sys
from PySide6.QtWidgets import QApplication
from src.calculadora import CalculadoraWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraWindow()
    window.show()
    sys.exit(app.exec())
