import sys 
from  PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit,QLabel,QMessageBox)

def perform_operation(operation):
    try:
        num1 = float(entrada1.text())
        num2 = float(entrada2.text())
        if operation == 'add':
            result = num1 + num2
            QMessageBox.information(ventana, "Resultado", f"La suma es: {result}")
        elif operation == 'subtract':
            result = num1 - num2
            QMessageBox.information(ventana, "Resultado", f"La resta es: {result}")
        elif operation == 'multiply':
            result = num1 * num2
            QMessageBox.information(ventana, "Resultado", f"La multiplicación es: {result}")
        elif operation == 'divide':
            if num2 == 0:
                QMessageBox.warning(ventana, "Error", "No se puede dividir por cero")
                return
            result = num1 / num2
            QMessageBox.information(ventana, "Resultado", f"La división es: {result}")
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor, ingrese números válidos")

# Creacion de la aplicacion

app = QApplication(sys.argv)



def mensaje():
    info = entrada1.text()
    QMessageBox.information(ventana, "Mensaje", info)
    
# Creacion de la ventana

ventana = QWidget()
ventana.setWindowTitle("Calculadora Básica") # Titulo de la ventana
ventana.resize(600, 600) # Tamaño de la ventana
ventana.show ()


# Creacion de los elementos de la ventana

label1 = QLabel("Escribe el primer número:")
label2 = QLabel("Escribe el segundo número:")
entrada1 = QLineEdit()
entrada2 = QLineEdit()
boton_suma = QPushButton("Sumar")
boton_resta = QPushButton("Restar")
boton_multiplicacion = QPushButton("Multiplicar")
boton_division = QPushButton("Dividir")


# Connect buttons to the perform_operation function
boton_suma.clicked.connect(lambda: perform_operation('add'))
boton_resta.clicked.connect(lambda: perform_operation('subtract'))
boton_multiplicacion.clicked.connect(lambda: perform_operation('multiply'))
boton_division.clicked.connect(lambda: perform_operation('divide'))

# Add widgets to the layout
layout = QVBoxLayout()

layout.addWidget(label1)
layout.addWidget(entrada1)
layout.addWidget(label2)
layout.addWidget(entrada2)
layout.addWidget(boton_suma)
layout.addWidget(boton_resta)
layout.addWidget(boton_multiplicacion)
layout.addWidget(boton_division)

# Set the layout for the window
ventana.setLayout(layout)

# Show the window
ventana.show()

# Start the application
sys.exit(app.exec_())




# Hacer una ventanita que permita hacer las 4 operaciones basicas. 



