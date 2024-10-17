# QtGui QTCore QtWidgets
# ============== Cara 1 ============================================
from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication([])
Window = QtWidgets.QPushButton("MyButton")
Window.show()
app.exec_()