__author__ = 'wil_jm'

from APIarduino.arduino import Arduino
import time
import sys
from PyQt4 import QtGui, uic, QtCore

class Demo(QtGui.QMainWindow):

    def __init__(self):
        super(Demo, self).__init__()
        self.var=uic.loadUi('button.ui', self)
        self.var.pushButton.setText("OFF")
        self.b = Arduino('/dev/ttyACM1')
        self.pin = 13
        self.b.output([self.pin])

    @QtCore.pyqtSlot()
    def on_pushButton_pressed(self):# si presiona el boton, el led se enciende
        self.var.pushButton.setStyleSheet("background-color: red;")
        self.var.pushButton.setText("ON")
        self.b.setHigh(self.pin)



    @QtCore.pyqtSlot()
    def on_pushButton_released(self):# si deja de presionar el boton, el led se apaga
        self.var.pushButton.setStyleSheet("background-color: none;")
        self.var.pushButton.setText("OFF")
        self.b.setLow(self.pin)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Demo()
    ui.show()
    sys.exit(app.exec_())
