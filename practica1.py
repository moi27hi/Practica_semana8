import sys 
from  PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit,QLabel)

app = QApplication(sys.argv)
ventana = QWidget()
ventana.show ()
layout = QVBoxLayout()
label1 = QLabel("Esto es un texto")
boton1 = QPushButton("Haz click aqui")
entrada1 = QLineEdit()
layout.addWidget(label1)
layout.addWidget(boton1)
layout.addWidget(entrada1)
ventana.setLayout(layout)
sys.exit(app.exec_())

