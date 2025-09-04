# Calculator App

## Descripción
Calculadora básica desarrollada con PySide6 como proyecto de aprendizaje de interfaces gráficas en Python.

## Estado Actual
- ✅ Operaciones básicas (+, -, *, /)
- ✅ Botones numéricos (0-9)
- ✅ Manejo de números decimales
- ✅ Botón Clear (C)
- ✅ Botón Delete (borrar último dígito)
- ✅ Botón Porcentaje (% simple y con operadores)
- ✅ Manejo de errores (división por cero)
- ✅ Doble display (historial y resultado)
- ✅ Formateo de números con separadores de miles
- ✅ Soporte para números de hasta 16 dígitos
- ✅ **Soporte completo de teclado (ES-LA)** (NEW!)

## Controles de Teclado ⌨️ (Español Latinoamericano)
### Números
- **0-9**: Entrada numérica
- **. (Punto)**: Decimal

### Operaciones Básicas
- **+ (Plus)**: Suma
- **- (Minus)**: Resta
- **Enter/Return**: Calcular resultado
- **Escape**: Limpiar calculadora (Clear)
- **Backspace**: Borrar último dígito

### Operaciones Avanzadas (con Shift)
- **Shift + +**: Multiplicación (×)
- **Shift + 7**: División (÷)
- **Shift + 5**: Porcentaje (%)
- **Shift + =**: Calcular resultado alternativo

## Tecnologías
- Python 3.11.5
- PySide6
- Qt Designer

## Roadmap

### 1. Funcionalidad básica ✅ COMPLETADO
- ✅ Operaciones aritméticas básicas
- ✅ Manejo de decimales y formateo
- ✅ Funciones de utilidad (Clear, Delete, Porcentaje)

### 2. Mejorar UX significativamente ✅ COMPLETADO
- ✅ Doble display
- ✅ Inicializar con "0"
- ✅ **Soporte completo de teclado (ES-LA)**

### 3. Mejora de Diseño 🎨
- ⏳ Styling visual
- ⏳ Visual feedback cuando se presionan teclas

### 4. Empaquetado 📦
- ⏳ Crear ejecutable para distribución

## Características Técnicas
- **Precisión**: Soporte para números de hasta 16 dígitos
- **Formateo**: Separadores de miles automáticos
- **Validación**: Límites de entrada para prevenir overflow
- **Manejo de errores**: División por cero y syntax errors
- **Arquitectura**: Separación clara entre UI y lógica
- **Accesibilidad**: Control completo por teclado español latinoamericano
- **UX**: Sin foco visual en botones para evitar interferencias

## Arquitectura del Código
```
calculator/
├── main.py                 # Punto de entrada
├── src/
│   └── calculadora.py     # Lógica principal de la calculadora
├── ui_generated/          # UI generada por Qt Designer
│   └── calculadora_ui.py
├── ui/                     # Archivo de diseño Qt Designer
│   └── calculadora.ui
└── 
```

### Métodos Principales
- `keyPressEvent()`: Manejo de entrada por teclado
- `on_number_clicked()`: Procesamiento de dígitos
- `on_operator_clicked()`: Operaciones matemáticas
- `equal_operand()`: Cálculo de resultados
- `format_number()`: Formateo visual de números

## Documentación
- Código documentado con docstrings en español
- Funciones principales comentadas
- Validaciones y límites bien definidos
- Mapeo claro de teclas a funciones

## Próximos Pasos
1. **Visual feedback**: Animaciones y efectos visuales al presionar teclas
2. **Mejoras de diseño**: Gradientes, sombras, mejores colores
3. **Empaquetado**: Crear ejecutable standalone

---

*Proyecto desarrollado como parte del aprendizaje de PySide6 y desarrollo de interfaces gráficas.*