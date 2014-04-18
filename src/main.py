__author__ = 'Marcin'

import sys
import os

from lcp.gui.gui import *
from lcp.parser.grammar import *

if __name__ == "__main__":
    ########################### delete this #############################
    os.system("pyuic4 lcp\gui\ui\main_window.ui > lcp\gui\main_window.py")
    #####################################################################

    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())