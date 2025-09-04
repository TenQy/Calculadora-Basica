from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QPushButton

class ButtonAnimator:
    """Clase para manejar animaciones de botones de la calculadora."""
    def __init__(self):
        self.animations = {}

    def create_scale_animation(self, button: QPushButton, duration: int = 100):
        """
        Crea una animación de escala para un botón.
        
        Args:
            button (QPushButton): El botón a animar
            duration (int): Duración de la animación en milisegundos
        """
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(duration)

        original_geometry = button.geometry()
        scale_factor = 0.95

        new_width = int(original_geometry.width() * scale_factor)
        new_height = int(original_geometry.height() * scale_factor)

        offset_x = (original_geometry.width() - new_width) // 2
        offset_y = (original_geometry.height() - new_height) // 2

        reduced_geometry = original_geometry.adjusted(offset_x, offset_y, -offset_x, -offset_y)

        animation.setKeyValueAt(0.0, original_geometry)
        animation.setKeyValueAt(0.5, reduced_geometry)
        animation.setKeyValueAt(1.0, original_geometry)

        animation.setEasingCurve(QEasingCurve.Type.Linear)

        self.animations[id(button)] = animation

        return animation
    
    def animation_button_click(self, button: QPushButton):
        """
        Ejecuta la animación de click en un botón.
        
        Args:
            button (QPushButton): El botón a animar
        """
        animation = self.create_scale_animation(button)
        animation.start()