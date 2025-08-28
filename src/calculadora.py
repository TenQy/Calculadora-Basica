from PySide6.QtWidgets import QMainWindow
from ui_generated.calculadora_ui import Ui_MainWindow

class CalculadoraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculadora")

        self.setFixedSize(326, 400)
        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().availableGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)