__author__ = 'Marcin'

import sys

from lcp.gui.gui import *
from lcp.parser.grammar import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())