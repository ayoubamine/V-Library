# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_categories.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(311, 321)
        Dialog.setMinimumSize(QtCore.QSize(311, 321))
        Dialog.setMaximumSize(QtCore.QSize(311, 321))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("/*\n"
"    QDialog\n"
"*/\n"
"\n"
"QDialog#Dialog\n"
"{\n"
"    background-color: white\n"
"}\n"
"\n"
"/*\n"
"    QPushButton\n"
"*/\n"
"\n"
"QPushButton#cancel\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QPushButton#cancel:hover\n"
"{\n"
"    background-color: #f2f2f2\n"
"}\n"
"\n"
"QPushButton#go\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: #B0BEC5;\n"
"    border-radius: 2px;\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton#go:hover\n"
"{\n"
"    background-color: #90A4AE\n"
"}\n"
"\n"
"/*\n"
"    QListWidget\n"
"*/\n"
"\n"
"QListWidget\n"
"{\n"
"    color:#607D8B;\n"
"    background-color: white;\n"
"    border-top: 0px\n"
"}\n"
"\n"
"QListWidget:item\n"
"{\n"
"    background-color: #f2f2f2;\n"
"    margin-bottom:1px;\n"
"    padding:5px;\n"
"    height: 27px;\n"
"    border-radius: 0px\n"
"}\n"
"\n"
"QListWidget:item:hover\n"
"{\n"
"    background-color: #ECEFF1;\n"
"    border: 0px\n"
"}\n"
"\n"
"QListWidget:item:selected\n"
"{\n"
"    background-color: #ECEFF1;\n"
"    color:#607D8B\n"
"}\n"
"\n"
"/*\n"
"    QScrollBar\n"
"*/\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #eceff1;\n"
"    width: 5px;    \n"
"    margin: 0;\n"
"    border: 0\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #b0bec5;\n"
"    min-height: 15px;\n"
"    border-radius: 2px\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height: 0px\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height: 0px\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color: #eceff1;\n"
"    height: 5px;    \n"
"    margin: 0;\n"
"    border: 0\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #b0bec5;\n"
"    min-width: 15px;\n"
"    border-radius: 2px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    width: 0px\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    width: 0px\n"
"}"))
        self.go = QtGui.QPushButton(Dialog)
        self.go.setGeometry(QtCore.QRect(10, 280, 91, 31))
        self.go.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/image/Upload_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go.setIcon(icon1)
        self.go.setObjectName(_fromUtf8("go"))
        self.categories = QtGui.QListWidget(Dialog)
        self.categories.setGeometry(QtCore.QRect(10, 10, 291, 261))
        self.categories.setStyleSheet(_fromUtf8(""))
        self.categories.setFrameShape(QtGui.QFrame.NoFrame)
        self.categories.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.categories.setProperty("isWrapping", False)
        self.categories.setObjectName(_fromUtf8("categories"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(210, 280, 91, 29))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/image/Delete_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon2)
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.go.setText(_translate("Dialog", "Go !", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))

import ui.images_rc
