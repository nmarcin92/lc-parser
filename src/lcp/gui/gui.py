__author__ = 'Marcin'

import sys

from PyQt4 import QtGui

from main_window import Ui_MainWindow
from ..parser.grammar import Grammar


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.grammar = Grammar()
        self.file_name = ''

        self.ui.parseGrammarButton.clicked.connect(self.on_parse_grammar_click)
        self.ui.actionNew.triggered.connect(self.on_new_click)
        self.ui.actionLoad.triggered.connect(self.on_load_click)
        self.ui.actionSave.triggered.connect(self.on_save_click)
        self.ui.actionSave_as.triggered.connect(self.on_save_as_click)
        self.ui.actionExit.triggered.connect(self.on_exit)

        self.ui.actionSave.setEnabled(False)

    def on_parse_grammar_click(self):
        self.grammar = Grammar()
        self.grammar.parse_from_text(str(self.ui.grammarTextEdit.toPlainText()))
        self.ui.grammarTextEdit.setText(self.grammar.to_plain_text())

    def on_new_click(self):
        self.grammar = Grammar()
        self.file_name = ''
        self.ui.grammarTextEdit.clear()
        self.ui.actionSave.setEnabled(False)

    def on_load_click(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', filter="Grammar files (*.grm)")
        if file_name != '':
            f = open(file_name, 'r')
            self.ui.grammarTextEdit.setText(f.read())
            f.close()

            self.file_name = file_name
            self.ui.actionSave.setEnabled(True)

    def on_save_click(self):
        f = open(self.file_name, 'w')
        f.write(str(self.ui.grammarTextEdit.toPlainText()))
        f.close()

    def on_save_as_click(self):
        file_name = QtGui.QFileDialog.getSaveFileName(self, 'Save to file', filter="Grammar files (*.grm)")
        if file_name != '':
            f = open(file_name, 'w')
            f.write(str(self.ui.grammarTextEdit.toPlainText()))
            f.close()
            self.file_name = file_name

    def on_exit(self):
        sys.exit(0)