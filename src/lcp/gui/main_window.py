# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcp\gui\ui\main_window.ui'
#
# Created: Fri Apr 18 18:43:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 523)
        MainWindow.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.grammarTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.grammarTextEdit.setGeometry(QtCore.QRect(10, 30, 311, 351))
        self.grammarTextEdit.setObjectName(_fromUtf8("grammarTextEdit"))
        self.parserTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.parserTableWidget.setGeometry(QtCore.QRect(330, 30, 451, 381))
        self.parserTableWidget.setObjectName(_fromUtf8("parserTableWidget"))
        self.parserTableWidget.setColumnCount(0)
        self.parserTableWidget.setRowCount(0)
        self.grammarLabel = QtGui.QLabel(self.centralwidget)
        self.grammarLabel.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.grammarLabel.setObjectName(_fromUtf8("grammarLabel"))
        self.parserTableLabel = QtGui.QLabel(self.centralwidget)
        self.parserTableLabel.setGeometry(QtCore.QRect(330, 10, 81, 16))
        self.parserTableLabel.setObjectName(_fromUtf8("parserTableLabel"))
        self.wordLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.wordLineEdit.setGeometry(QtCore.QRect(390, 420, 301, 20))
        self.wordLineEdit.setObjectName(_fromUtf8("wordLineEdit"))
        self.transformGrammarButton = QtGui.QPushButton(self.centralwidget)
        self.transformGrammarButton.setGeometry(QtCore.QRect(170, 390, 141, 23))
        self.transformGrammarButton.setObjectName(_fromUtf8("transformGrammarButton"))
        self.generateTableButton = QtGui.QPushButton(self.centralwidget)
        self.generateTableButton.setGeometry(QtCore.QRect(10, 420, 301, 31))
        self.generateTableButton.setObjectName(_fromUtf8("generateTableButton"))
        self.checkWordButton = QtGui.QPushButton(self.centralwidget)
        self.checkWordButton.setGeometry(QtCore.QRect(710, 420, 75, 23))
        self.checkWordButton.setObjectName(_fromUtf8("checkWordButton"))
        self.enterWordLabel = QtGui.QLabel(self.centralwidget)
        self.enterWordLabel.setGeometry(QtCore.QRect(330, 420, 61, 16))
        self.enterWordLabel.setObjectName(_fromUtf8("enterWordLabel"))
        self.parseGrammarButton = QtGui.QPushButton(self.centralwidget)
        self.parseGrammarButton.setGeometry(QtCore.QRect(10, 390, 141, 23))
        self.parseGrammarButton.setObjectName(_fromUtf8("parseGrammarButton"))
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 460, 391, 21))
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 460, 46, 21))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LC Parser Visualizer", None))
        self.grammarTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.grammarLabel.setText(_translate("MainWindow", "Grammar:", None))
        self.parserTableLabel.setText(_translate("MainWindow", "LC Parser table:", None))
        self.transformGrammarButton.setText(_translate("MainWindow", "Transform grammar", None))
        self.generateTableButton.setText(_translate("MainWindow", "Genarate table", None))
        self.checkWordButton.setText(_translate("MainWindow", "Check", None))
        self.enterWordLabel.setText(_translate("MainWindow", "Enter word:", None))
        self.parseGrammarButton.setText(_translate("MainWindow", "Parse grammar", None))
        self.label.setText(_translate("MainWindow", "Status:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

