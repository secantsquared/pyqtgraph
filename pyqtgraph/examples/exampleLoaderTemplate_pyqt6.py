# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'examples/exampleLoaderTemplate.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 552)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.qtLibCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.qtLibCombo.setObjectName("qtLibCombo")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.gridLayout.addWidget(self.qtLibCombo, 4, 1, 1, 1)
        self.loadBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 6, 1, 1, 1)
        self.exampleTree = QtWidgets.QTreeWidget(self.layoutWidget)
        self.exampleTree.setObjectName("exampleTree")
        self.exampleTree.headerItem().setText(0, "1")
        self.exampleTree.header().setVisible(False)
        self.gridLayout.addWidget(self.exampleTree, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.exampleFilter = QtWidgets.QLineEdit(self.layoutWidget)
        self.exampleFilter.setObjectName("exampleFilter")
        self.gridLayout.addWidget(self.exampleFilter, 0, 0, 1, 2)
        self.searchFiles = QtWidgets.QComboBox(self.layoutWidget)
        self.searchFiles.setObjectName("searchFiles")
        self.searchFiles.addItem("")
        self.searchFiles.addItem("")
        self.gridLayout.addWidget(self.searchFiles, 1, 0, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadedFileLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        self.loadedFileLabel.setFont(font)
        self.loadedFileLabel.setText("")
        self.loadedFileLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadedFileLabel.setObjectName("loadedFileLabel")
        self.verticalLayout.addWidget(self.loadedFileLabel)
        self.codeView = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.codeView.setFont(font)
        self.codeView.setObjectName("codeView")
        self.verticalLayout.addWidget(self.codeView)
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQtGraph"))
        self.qtLibCombo.setItemText(0, _translate("Form", "default"))
        self.qtLibCombo.setItemText(1, _translate("Form", "PyQt5"))
        self.qtLibCombo.setItemText(2, _translate("Form", "PySide2"))
        self.qtLibCombo.setItemText(3, _translate("Form", "PySide6"))
        self.qtLibCombo.setItemText(4, _translate("Form", "PyQt6"))
        self.loadBtn.setText(_translate("Form", "Run Example"))
        self.label.setText(_translate("Form", "Qt Library:"))
        self.exampleFilter.setPlaceholderText(_translate("Form", "Type to filter..."))
        self.searchFiles.setItemText(0, _translate("Form", "Title Search"))
        self.searchFiles.setItemText(1, _translate("Form", "Content Search"))
