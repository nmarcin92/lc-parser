__author__ = 'Marcin'

import sys
from PyQt4 import QtGui, QtCore
from gui.gui import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())