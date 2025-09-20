import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox)
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt

def desarrollar_conversion():
    try:
        num1 = float(entrada1.text())
        conversion_type = conversion_selector.currentText()
        
        if num1 < 0:
            QMessageBox.warning(ventana, "Error", "El valor no puede ser negativo")
            return
        
        if conversion_type == "Kilogramos a Libras":
            resultado = num1 * 2.20462
            QMessageBox.information(ventana, "Resultado", f"{num1} kg = {round(resultado, 2)} lb")
        elif conversion_type == "Libras a Kilogramos":
            resultado = num1 * 0.453592
            QMessageBox.information(ventana, "Resultado", f"{num1} lb = {round(resultado, 2)} kg")
        elif conversion_type == "Pies a Metros":
            resultado = num1 * 0.3048
            QMessageBox.information(ventana, "Resultado", f"{num1} pies = {round(resultado, 2)} metros")
        else:  # Metros a Pies
            resultado = num1 * 3.28084
            QMessageBox.information(ventana, "Resultado", f"{num1} metros = {round(resultado, 2)} pies")
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor, ingrese un número válido")

# Create the application
app = QApplication(sys.argv)

# Create the main window
ventana = QWidget()
ventana.setWindowTitle("Convertidor de Peso y Estatura")
ventana.resize(300, 200)

# Create layout
layout = QVBoxLayout()

# Create widgets
label1 = QLabel("Ingrese el valor a convertir:")
entrada1 = QLineEdit()
# Set validator to accept only non-negative numbers
validator = QDoubleValidator(0.0, 1000000.0, 10, notation=QDoubleValidator.StandardNotation)
entrada1.setValidator(validator)
conversion_selector = QComboBox()
conversion_selector.addItems([
    "Kilogramos a Libras",
    "Libras a Kilogramos",
    "Pies a Metros",
    "Metros a Pies"
])
convert_button = QPushButton("Convertir")

# Connect button to the conversion function
convert_button.clicked.connect(desarrollar_conversion)

# Add widgets to the layout
layout.addWidget(label1)
layout.addWidget(entrada1)
layout.addWidget(conversion_selector)
layout.addWidget(convert_button)

# Set the layout for the window
ventana.setLayout(layout)

# Show the window
ventana.show()

# Start the application
sys.exit(app.exec_())