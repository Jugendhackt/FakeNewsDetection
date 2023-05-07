import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PySide6.QtCore import Qt


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["output"]

        self.button = QtWidgets.QPushButton("search")
        self.e4 = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.e4 = QLineEdit()
        self.button.clicked.connect(self.textchanged)
        self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.layout.addWidget(self.e4)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        
        self.setWindowTitle("TpD")


    def textchanged(self):
        print(self.e4.text())


    





                

        
        



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())

