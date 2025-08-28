from PySide6.QtWidgets import QMainWindow
from ui_generated.calculadora_ui import Ui_MainWindow

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setFixedSize(326, 400)

        #Centrar en pantalla
        self.center_on_screen()

        #Conectar botones
        self.connect_buttons()

    def center_on_screen(self):
        screen = self.screen().availableGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def connect_buttons(self):
        self.ui.btn_0.clicked.connect(lambda: self.on_number_clicked("0"))
        self.ui.btn_1.clicked.connect(lambda: self.on_number_clicked("1"))
        self.ui.btn_2.clicked.connect(lambda: self.on_number_clicked("2"))
        self.ui.btn_3.clicked.connect(lambda: self.on_number_clicked("3"))
        self.ui.btn_4.clicked.connect(lambda: self.on_number_clicked("4"))
        self.ui.btn_5.clicked.connect(lambda: self.on_number_clicked("5"))
        self.ui.btn_6.clicked.connect(lambda: self.on_number_clicked("6"))
        self.ui.btn_7.clicked.connect(lambda: self.on_number_clicked("7"))
        self.ui.btn_8.clicked.connect(lambda: self.on_number_clicked("8"))
        self.ui.btn_9.clicked.connect(lambda: self.on_number_clicked("9"))

    def on_number_clicked(self, number):
        current_text = self.ui.display.text()
        new_text = current_text + number
        self.ui.display.setText(new_text)
