# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
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
        Dialog.resize(581, 375)
        Dialog.setMinimumSize(QtCore.QSize(581, 375))
        Dialog.setMaximumSize(QtCore.QSize(581, 375))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("/*\n"
"    QDialog\n"
"*/\n"
"\n"
"QDialog#Dialog\n"
"{\n"
"    background: white\n"
"}\n"
"\n"
"/*\n"
"    QLabel\n"
"*/\n"
"\n"
"QLabel#label_2,\n"
"QLabel#version,\n"
"QLabel#label_4,\n"
"QLabel#label_6,\n"
"QLabel#label_10\n"
"{color: #607D8B}\n"
"QLabel#email,\n"
"QLabel#github\n"
"{color: rgb(144, 144, 144)}\n"
"QLabel#label_9,\n"
"QLabel#label_5\n"
"{color: #51b6f5}\n"
"QLabel#label\n"
"{color: grey}\n"
"\n"
"/*\n"
"    QPushButton\n"
"*/\n"
"\n"
"QPushButton#license,\n"
"QPushButton#backup,\n"
"QPushButton#restore\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QPushButton#license:hover,\n"
"QPushButton#backup:hover,\n"
"QPushButton#restore:hover\n"
"{\n"
"    background-color: #f2f2f2\n"
"}\n"
"\n"
"/*\n"
"    QTabWidget\n"
"*/\n"
"\n"
"QTabWidget::pane\n"
"{\n"
"    border-top: 1px solid #f5f6f7\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background: white;\n"
"    border-bottom-color: #C2C7CB;\n"
"    height: 40;\n"
"    padding:0 4px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover\n"
"{\n"
"    background: #f5f6f7\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB\n"
"}"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 581, 401))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.logo = QtGui.QLabel(self.tab)
        self.logo.setGeometry(QtCore.QRect(130, 20, 131, 121))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.png")))
        self.logo.setScaledContents(False)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.version = QtGui.QLabel(self.tab)
        self.version.setGeometry(QtCore.QRect(370, 90, 61, 21))
        self.version.setObjectName(_fromUtf8("version"))
        self.license = QtGui.QPushButton(self.tab)
        self.license.setGeometry(QtCore.QRect(250, 300, 101, 29))
        self.license.setObjectName(_fromUtf8("license"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(140, 230, 16, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(160, 230, 71, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(140, 260, 16, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(160, 260, 71, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.email = QtGui.QLabel(self.tab)
        self.email.setGeometry(QtCore.QRect(240, 260, 221, 17))
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.email.setStyleSheet(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.github = QtGui.QLabel(self.tab)
        self.github.setGeometry(QtCore.QRect(240, 230, 221, 16))
        self.github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.github.setStyleSheet(_fromUtf8(""))
        self.github.setWordWrap(False)
        self.github.setObjectName(_fromUtf8("github"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 164, 401, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/About_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.backup = QtGui.QPushButton(self.tab_3)
        self.backup.setGeometry(QtCore.QRect(100, 140, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backup.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Database_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backup.setIcon(icon2)
        self.backup.setIconSize(QtCore.QSize(24, 24))
        self.backup.setObjectName(_fromUtf8("backup"))
        self.restore = QtGui.QPushButton(self.tab_3)
        self.restore.setGeometry(QtCore.QRect(360, 140, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restore.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Download_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore.setIcon(icon3)
        self.restore.setIconSize(QtCore.QSize(24, 24))
        self.restore.setObjectName(_fromUtf8("restore"))
        self.loader = QtGui.QLabel(self.tab_3)
        self.loader.setGeometry(QtCore.QRect(265, 145, 51, 51))
        self.loader.setText(_fromUtf8(""))
        self.loader.setScaledContents(False)
        self.loader.setObjectName(_fromUtf8("loader"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Database_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon4, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About V-Library", None))
        self.label_2.setText(_translate("Dialog", "V-Library", None))
        self.version.setText(_translate("Dialog", "V 1.0", None))
        self.license.setText(_translate("Dialog", "License", None))
        self.label_4.setText(_translate("Dialog", "Ayoub Amine", None))
        self.label_5.setText(_translate("Dialog", "//", None))
        self.label_6.setText(_translate("Dialog", "Web Site :", None))
        self.label_9.setText(_translate("Dialog", "//", None))
        self.label_10.setText(_translate("Dialog", "e-mail :", None))
        self.email.setText(_translate("Dialog", "programmer010011@gmail.com", None))
        self.github.setText(_translate("Dialog", "v-library.github.io", None))
        self.label.setText(_translate("Dialog", "V-Library is free and open source software created by:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "About", None))
        self.backup.setText(_translate("Dialog", "Backup", None))
        self.restore.setText(_translate("Dialog", "Restore", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Backup/Restore", None))

import ui.images_rc
