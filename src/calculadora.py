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

        #Variables para guardar informacion
        self.reset_calculator()

    def center_on_screen(self):
        """Centra la aplicación en la pantalla."""
        screen = self.screen().availableGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def connect_buttons(self):
        """Conecta la funcionalidad de todos los botones de la calculadora."""
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

        self.ui.btn_dot.clicked.connect(self.on_dot_clicked)
        self.ui.btn_clear.clicked.connect(self.clear_display)

        self.ui.btn_plus.clicked.connect(lambda: self.on_operator_clicked("+"))
        self.ui.btn_minus.clicked.connect(lambda: self.on_operator_clicked("-"))
        self.ui.btn_multiply.clicked.connect(lambda: self.on_operator_clicked("*"))
        self.ui.btn_divide.clicked.connect(lambda: self.on_operator_clicked("/"))

        self.ui.btn_equal.clicked.connect(self.equal_operand)

    def on_number_clicked(self, number):
        """
        Maneja el evento cuando se presiona un botón numérico.
        
        Args:
            number (str): El dígito presionado como string ("0"-"9")
        """
        if self.should_clear_display():
            self.ui.display.setText(number)
            self.waiting_for_operand = False
        else:
            current_text = self.ui.display.text()
            new_text = current_text + number
            self.ui.display.setText(new_text)

    def on_dot_clicked(self):
        """Maneja el evento cuando se presiona el botón del punto."""
        if self.should_clear_display():
            self.ui.display.setText("0.")
            self.waiting_for_operand = False
        else:
            current_text = self.ui.display.text() 
            if "." not in current_text:
                self.ui.display.setText(current_text + ".")

    def clear_display(self):
        """Limpia el display y reinicia la calculadora."""
        self.ui.display.setText("")
        self.reset_calculator()

    def should_clear_display(self):
        """
        Indica si debe limpiar el display antes del siguiente input.
        
        Returns: 
            bool: True si debe limpiarse, False en caso contrario
        """
        current_text = self.ui.display.text()
        return (self.waiting_for_operand or current_text == "Syntax Error")
    
    def reset_calculator(self):
        """Limpia todas las variables de inicio."""
        self.first_number = ""
        self.current_operator = ""
        self.waiting_for_operand = False

    def on_operator_clicked(self, operator):
        """
        Maneja el evento cuando se presiona un operador aritmético.

        Args:
            operator (str): El operador presionado ("+","-","*","/")
        """
        self.first_number = self.ui.display.text()
        self.current_operator = operator
        self.waiting_for_operand = True
    
    def equal_operand(self):
        """Calcula y muestra el resultado de la operación aritmética actual."""
        if not self.first_number or not self.current_operator:
            return
        
        try:
            first_num = float(self.first_number)
            second_num = float(self.ui.display.text())

            if self.current_operator == "+":
                result = first_num + second_num
            elif self.current_operator == "-":
                result = first_num - second_num
            elif self.current_operator == "*":
                result = first_num * second_num
            elif self.current_operator == "/":
                if second_num != 0:
                    result = first_num / second_num
                else:
                    self.ui.display.setText("Syntax Error")
                    self.reset_calculator()
                    return
            
            if result == int(result):
                formatted_result = str(int(result))
            else:
                formatted_result = str(result)

            self.ui.display.setText(str(formatted_result))
            self.reset_calculator()
            self.waiting_for_operand = True

        except ValueError:
            self.ui.display.setText("Syntax Error")
            self.reset_calculator()