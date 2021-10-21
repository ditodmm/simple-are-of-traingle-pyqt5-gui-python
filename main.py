import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi

class luassegitiga(QMainWindow):
	def __init__(self):
		super().__init__()
		loadUi("ui.ui",self)
		self.btnhitung.clicked.connect(self.hitungfunction)

	def hitungfunction(self):
		alas = float(self.txtalas.text())
		tinggi = float(self.txttinggi.text())
		luas = 0.5 * alas * tinggi
		self.txthasil.setText(str(luas))
		self.txtalas.setText("")
		self.txttinggi.setText("")

app=QApplication(sys.argv)
mainwindow=luassegitiga()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Luas Segitiga")
widget.setFixedWidth(300)
widget.setFixedHeight(250)
widget.show()
app.exec_()
