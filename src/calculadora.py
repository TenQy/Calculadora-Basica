from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui_generated.calculadora_ui import Ui_MainWindow
from .animaciones import ButtonAnimator

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setFixedSize(330, 400)

        #Centrar en pantalla
        self.center_on_screen()

        #Conectar botones
        self.connect_buttons()

        #Variables para guardar informacion
        self.reset_calculator()

        #Crear variable para animaciones
        self.animator = ButtonAnimator()

    def center_on_screen(self):
        """Centra la aplicación en la pantalla."""
        screen = self.screen().availableGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def connect_buttons(self):
        """Conecta la funcionalidad de todos los botones de la calculadora."""
        self.ui.btn_0.clicked.connect(lambda: self.animated_number_click("0"))
        self.ui.btn_1.clicked.connect(lambda: self.animated_number_click("1"))
        self.ui.btn_2.clicked.connect(lambda: self.animated_number_click("2"))
        self.ui.btn_3.clicked.connect(lambda: self.animated_number_click("3"))
        self.ui.btn_4.clicked.connect(lambda: self.animated_number_click("4"))
        self.ui.btn_5.clicked.connect(lambda: self.animated_number_click("5"))
        self.ui.btn_6.clicked.connect(lambda: self.animated_number_click("6"))
        self.ui.btn_7.clicked.connect(lambda: self.animated_number_click("7"))
        self.ui.btn_8.clicked.connect(lambda: self.animated_number_click("8"))
        self.ui.btn_9.clicked.connect(lambda: self.animated_number_click("9"))

        self.ui.btn_dot.clicked.connect(self.on_dot_clicked)
        self.ui.btn_clear.clicked.connect(self.reset_calculator)
        self.ui.btn_delete.clicked.connect(self.on_delete_clicked)
        self.ui.btn_percent.clicked.connect(self.on_percent_clicked)

        self.ui.btn_plus.clicked.connect(lambda: self.on_operator_clicked("+"))
        self.ui.btn_minus.clicked.connect(lambda: self.on_operator_clicked("-"))
        self.ui.btn_multiply.clicked.connect(lambda: self.on_operator_clicked("x"))
        self.ui.btn_divide.clicked.connect(lambda: self.on_operator_clicked("÷"))

        self.ui.btn_equal.clicked.connect(self.equal_operand)

    def keyPressEvent(self, event):
        """
        Maneja los eventos de teclado para la calculadora.
        
        Args:
            event (QKeyEvent): Evento de tecla presionada
        """
        key = event.key()
        
        number_keys = {
            Qt.Key.Key_0: "0",
            Qt.Key.Key_1: "1",
            Qt.Key.Key_2: "2",
            Qt.Key.Key_3: "3",
            Qt.Key.Key_4: "4",
            Qt.Key.Key_5: "5",
            Qt.Key.Key_6: "6",
            Qt.Key.Key_7: "7",
            Qt.Key.Key_8: "8",
            Qt.Key.Key_9: "9"
        }

        if key in number_keys:
            self.on_number_clicked(number_keys[key])

        operator_keys = {
            Qt.Key.Key_Plus: "+",
            Qt.Key.Key_Minus: "-",
        }

        if key in operator_keys:
            self.on_operator_clicked(operator_keys[key])

        if key == Qt.Key.Key_Period:
            self.on_dot_clicked()
        elif key == Qt.Key.Key_Backspace:
            self.on_delete_clicked()
        elif key == Qt.Key.Key_Escape:
            self.reset_calculator()
        elif key == Qt.Key.Key_Enter or key == Qt.Key.Key_Return:
            self.equal_operand()

        modifiers = event.modifiers()
        shift_pressed = modifiers & Qt.KeyboardModifier.ShiftModifier

        if shift_pressed:
            shift_operators = {
                Qt.Key.Key_Slash: "÷",
                Qt.Key.Key_Asterisk: "x"
            }

            if key in shift_operators:
                self.on_operator_clicked(shift_operators[key])
            
            if key == Qt.Key.Key_Percent:
                self.on_percent_clicked()
            elif key == Qt.Key.Key_Equal:
                self.equal_operand()

        return super().keyPressEvent(event)
    
    def animated_number_click(self, number):
        """
        Wrapper que anima el botón y ejecuta la lógica del número.
        
        Args:
            number (str): El dígito presionado
        """
        button_map = {
            "0": self.ui.btn_0,
            "1": self.ui.btn_1,
            "2": self.ui.btn_2,
            "3": self.ui.btn_3,
            "4": self.ui.btn_4,
            "5": self.ui.btn_5,
            "6": self.ui.btn_6,
            "7": self.ui.btn_7,
            "8": self.ui.btn_8,
            "9": self.ui.btn_9
        }

        if number in button_map:
            self.animator.animation_button_click(button_map[number])
        
        self.on_number_clicked(number)

    def on_number_clicked(self, number):
        """
        Maneja el evento cuando se presiona un botón numérico.
        
        Args:
            number (str): El dígito presionado como string ("0"-"9")
        """

        if self.just_calculated:
            self.reset_calculator()

        if self.should_clear_display():
            self.update_display(number)
            self.waiting_for_operand = False
        else:
            current_text = self.ui.main_display.text()
            
            if self.is_within_input_limit(current_text, number):
                new_text = current_text + number
                self.update_display(new_text)

    def on_dot_clicked(self):
        """Maneja el evento cuando se presiona el botón del punto."""
        if self.just_calculated:
            self.reset_calculator()
            self.update_display("0.")
            return

        if self.should_clear_display():
            self.update_display("0.")
            self.waiting_for_operand = False
        else:
            current_text = self.ui.main_display.text() 
            clean_text = current_text.replace(",", "")

            if "." not in clean_text and self.is_within_input_limit(current_text, "."):
                new_text = clean_text + "."
                self.update_display(new_text)

    def on_delete_clicked(self):
        """Borra el último digito del número actual en el display."""
        if self.just_calculated:
            return
        
        current_text = self.ui.main_display.text()

        if not current_text or current_text == "Syntax Error":
            return
        
        if len(current_text) == 1:
            self.update_display("0")
        else:
            new_text = current_text[:-1]
            self.update_display(new_text)
        
    def on_percent_clicked(self):
        """
        Maneja el cálculo de porcentaje según el contexto actual.
        
        Si no hay operador: convierte el número a porcentaje (divide por 100)
        Si hay operador: calcula el porcentaje del primer número
        """
        if self.just_calculated and not self.current_operator:
            self.just_calculated = False
            self.ui.history_display.setText("")

        current_text = self.ui.main_display.text()

        if not current_text or current_text == "Syntax Error":
            return
        
        try:
            current_number = self.get_numeric_value(current_text)

            if not self.current_operator or not self.first_number:
                result = current_number / 100
                self.ui.history_display.setText("")
            else:
                base_number = float(self.first_number)
                result = (current_number / 100) * base_number

                percent_display = str(int(current_number)) if current_number == int(current_number) else str(current_number)
                base_display = str(int(base_number)) if base_number == int(base_number) else str(base_number)

                self.operation_history = f"{base_display} {self.current_operator} {percent_display}% of {base_display}"
                self.ui.history_display.setText(self.operation_history)

            self.update_display(result)

        except ValueError:            
            self.reset_calculator()
            self.ui.main_display.setText("Syntax Error")

    def should_clear_display(self):
        """
        Indica si debe limpiar el display antes del siguiente input.
        
        Returns: 
            bool: True si debe limpiarse, False en caso contrario
        """
        current_text = self.ui.main_display.text()
        return (self.waiting_for_operand or current_text == "Syntax Error" or current_text == "0")
    
    def reset_calculator(self):
        """Limpia todas las variables de inicio."""
        self.first_number = ""
        self.current_operator = ""
        self.waiting_for_operand = False
        self.operation_history = ""
        self.just_calculated = False

        self.ui.history_display.setText("")
        self.ui.main_display.setText("0")

    def is_numeric_string(self, text):
        """
        Verifica si un string representa un número válido.
        Acepta números con comas como separadores de miles.
        """
        if not isinstance(text, str):
            return False
        
        clean_text = text.replace(",", "").strip()

        try:
            float(clean_text)
            return True
        except ValueError:
            return False      

    def format_number(self, number):
        """
        Formatea números con separadores de miles.
        
        Args:
            number: Número a formatear (float, int, o str)
        
        Returns:
            str: Número formateado con comas
        """
        if isinstance(number, str):
            clean_number = number.replace(",", "")
            try:
                number = float(clean_number)
            except ValueError:
                return number
            
            if clean_number.endswith("."):
                integer_part = clean_number[:-1]
                formatted = f"{int(integer_part):,}."
                return formatted

        if number == int(number):
            formatted = f"{int(number):,}"
        else:
            formatted = f"{number:,.16g}"

        clean_formatted = formatted.replace(",", "")

        if len(clean_formatted) > 17:
            return f"{number:.6e}"
        
        return formatted

    def update_display(self, value):
        """
        Actualiza el display principal con formato y ajuste de fuente.
        
        Args:
            value: Valor a mostrar (número o string)
        """
        if isinstance(value, (int, float)) or self.is_numeric_string(value):
            formatted_text = self.format_number(value)
        else:
            formatted_text = str(value)

        self.ui.main_display.setText(formatted_text)

    def is_within_input_limit(self, current_text, new_char=""):
        """
        Verifica si el input está dentro del límite permitido.
        
        Args:
            current_text (str): Texto actual en el display
            new_char (str): Carácter que se quiere añadir
        
        Returns:
            bool: True si está dentro del límite, False si no
        """
        
        clean_text = current_text.replace(",", "")
        test_text = clean_text + new_char

        digits_only = test_text.replace(".", "").replace("-", "")
        return len(digits_only) <= 16


    def on_operator_clicked(self, operator):
        """
        Maneja el evento cuando se presiona un operador aritmético.

        Args:
            operator (str): El operador presionado ("+","-","*","/")
        """
        if self.just_calculated:
            self.first_number = self.get_numeric_value(self.ui.main_display.text())
            self.just_calculated = False
        else:
            self.first_number = self.get_numeric_value(self.ui.main_display.text())

        self.current_operator = operator
        self.waiting_for_operand = True

        formatted_first = self.format_number(self.first_number)
        self.operation_history = f"{formatted_first} {operator}"
        self.ui.history_display.setText(self.operation_history)

    def get_numeric_value(self, text):
        """
        Extrae el valor numérico de un texto, removiendo formato.
        
        Args:
            text (str): Texto que puede contener comas
            
        Returns:
            float: Valor numérico sin formato
        """
        if isinstance(text, (int, float)):
            return float(text)
        
        clean_text = text.replace(",", "")

        try:
            return float(clean_text)
        except ValueError:
            raise ValueError(f"No se puede convertir '{text}' a número.")
    
    def equal_operand(self):
        """Calcula y muestra el resultado de la operación aritmética actual."""
        if not self.first_number or not self.current_operator:
            return
        
        try:
            first_num = float(self.first_number)
            second_num = self.get_numeric_value(self.ui.main_display.text())

            if self.current_operator == "+":
                result = first_num + second_num
            elif self.current_operator == "-":
                result = first_num - second_num
            elif self.current_operator == "x":
                result = first_num * second_num
            elif self.current_operator == "÷":
                if second_num != 0:
                    result = first_num / second_num
                else:
                    self.reset_calculator()
                    self.ui.main_display.setText("Syntax Error")
                    return

            formatted_first = self.format_number(first_num)
            formatted_second = self.format_number(second_num)

            self.operation_history = f"{formatted_first} {self.current_operator} {formatted_second} ="
            self.ui.history_display.setText(self.operation_history)

            self.update_display(result)
            self.just_calculated = True

            self.first_number = ""
            self.current_operator = ""
            self.waiting_for_operand = False

        except ValueError:
            self.reset_calculator()
            self.ui.main_display.setText("Syntax Error")