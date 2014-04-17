__author__ = 'Marcin'

from PyQt4 import QtCore, QtGui

from main_window import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

