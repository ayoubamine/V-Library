# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_category.ui'
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
        Dialog.resize(411, 181)
        Dialog.setMinimumSize(QtCore.QSize(411, 181))
        Dialog.setMaximumSize(QtCore.QSize(411, 181))
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
" QLineEdit\n"
"*/\n"
"\n"
"QLineEdit\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"/*\n"
"    QPushButton\n"
"*/\n"
"\n"
"QPushButton#set__image,\n"
"QPushButton#delete__category,\n"
"QPushButton#save__info\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QPushButton#set__image:hover,\n"
"QPushButton#delete__category:hover,\n"
"QPushButton#save__info:hover\n"
"{\n"
"    background-color: #f2f2f2\n"
"}\n"
"\n"
"QPushButton#set__image\n"
"{\n"
"    border-radius: 0\n"
"}\n"
"\n"
"/*\n"
"    QToolButton\n"
"*/\n"
"\n"
"QToolButton#delete__image\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    border-radius: 0\n"
"}\n"
"\n"
"/*\n"
"    QLabel\n"
"*/\n"
"\n"
"QLabel\n"
"{\n"
"    color: #607D8B\n"
"}"))
        self.name = QtGui.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(20, 27, 41, 17))
        self.name.setObjectName(_fromUtf8("name"))
        self.icon = QtGui.QLabel(Dialog)
        self.icon.setGeometry(QtCore.QRect(20, 80, 61, 17))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.category__name = QtGui.QLineEdit(Dialog)
        self.category__name.setGeometry(QtCore.QRect(80, 20, 321, 31))
        self.category__name.setObjectName(_fromUtf8("category__name"))
        self.set__image = QtGui.QPushButton(Dialog)
        self.set__image.setGeometry(QtCore.QRect(110, 73, 91, 31))
        self.set__image.setObjectName(_fromUtf8("set__image"))
        self.delete__image = QtGui.QToolButton(Dialog)
        self.delete__image.setGeometry(QtCore.QRect(80, 73, 31, 31))
        self.delete__image.setStyleSheet(_fromUtf8(""))
        self.delete__image.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Delete_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete__image.setIcon(icon1)
        self.delete__image.setIconSize(QtCore.QSize(25, 25))
        self.delete__image.setObjectName(_fromUtf8("delete__image"))
        self.display__image = QtGui.QLabel(Dialog)
        self.display__image.setGeometry(QtCore.QRect(213, 76, 25, 25))
        self.display__image.setText(_fromUtf8(""))
        self.display__image.setScaledContents(True)
        self.display__image.setObjectName(_fromUtf8("display__image"))
        self.delete__category = QtGui.QPushButton(Dialog)
        self.delete__category.setGeometry(QtCore.QRect(10, 140, 141, 31))
        self.delete__category.setToolTip(_fromUtf8(""))
        self.delete__category.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Delete_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete__category.setIcon(icon2)
        self.delete__category.setObjectName(_fromUtf8("delete__category"))
        self.save__info = QtGui.QPushButton(Dialog)
        self.save__info.setGeometry(QtCore.QRect(330, 140, 71, 31))
        self.save__info.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Plus_18px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save__info.setIcon(icon3)
        self.save__info.setObjectName(_fromUtf8("save__info"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.category__name, self.save__info)
        Dialog.setTabOrder(self.save__info, self.delete__image)
        Dialog.setTabOrder(self.delete__image, self.delete__category)
        Dialog.setTabOrder(self.delete__category, self.set__image)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit/Delete Category", None))
        self.name.setText(_translate("Dialog", "Name :", None))
        self.icon.setText(_translate("Dialog", "Icon :", None))
        self.set__image.setText(_translate("Dialog", "Choose ...", None))
        self.delete__image.setToolTip(_translate("Dialog", "Delete icon", None))
        self.delete__category.setText(_translate("Dialog", "Delete Category", None))
        self.save__info.setText(_translate("Dialog", "Save", None))

import ui.images_rc
