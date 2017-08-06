# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_book.ui'
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
        Dialog.resize(391, 561)
        Dialog.setMinimumSize(QtCore.QSize(391, 561))
        Dialog.setMaximumSize(QtCore.QSize(391, 561))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("/*\n"
"    QDialog\n"
"*/\n"
"\n"
"QDialog#Dialog\n"
"{\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"/*\n"
"    QLabel\n"
"*/\n"
"\n"
"QLabel#label_title,\n"
"QLabel#label_author,\n"
"QLabel#move_to\n"
"{\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QLabel#notice\n"
"{\n"
"    color: #90A4AE\n"
"}\n"
"\n"
"QLabel#book__image\n"
"{\n"
"    border: 1px solid #f2f2f2\n"
"}\n"
"\n"
"/*\n"
"    QTextEdit\n"
"*/\n"
"\n"
"QTextEdit#note\n"
"{\n"
"    color: #607D8B\n"
"}\n"
"\n"
"/*\n"
"    QLineEdit\n"
"*/\n"
"\n"
"QLineEdit#title,\n"
"QLineEdit#authors\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B;\n"
"    padding: 0 4px\n"
"}\n"
"\n"
"/*\n"
"    QPushButton\n"
"*/\n"
"\n"
"QPushButton#change__image,\n"
"QPushButton#delete__image,\n"
"QPushButton#get__image,\n"
"QPushButton#reset__default\n"
"\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QPushButton#change__image:hover,\n"
"QPushButton#delete__image:hover,\n"
"QPushButton#get__image:hover,\n"
"QPushButton#reset__default:hover\n"
"{\n"
"    background-color: #f2f2f2\n"
"}\n"
"\n"
"QPushButton#save\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    background-color: #B0BEC5;\n"
"    border-radius: 2px;\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton#save:hover\n"
"{\n"
"    background-color: #90A4AE\n"
"}\n"
"\n"
"/*\n"
"    QComboBox\n"
"*/\n"
"\n"
"QComboBox\n"
"{\n"
"    color: #607D8B;\n"
"    background-color: rgb(240, 240, 240);\n"
"    border: 1px solid #cfd6e6;\n"
"    padding: 1px 0px 1px 3px; /*This makes text colour work*/\n"
"    border-radius: 2px;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    border-style: none;\n"
"    background-color: white\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border: 1px;\n"
"    border-color:#f2f2f2;\n"
"    border-left-style:solid;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/interface/image/Sort Down_16px.png);\n"
"    width: 16px;\n"
"    height: 16px\n"
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
"/*\n"
"    QTabBar\n"
"*/\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background: white;\n"
"    border-bottom-color: #C2C7CB;\n"
"    height: 40px;\n"
"    padding:0 4px;\n"
"    color: grey\n"
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
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 391, 561))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.reset__default = QtGui.QPushButton(self.tab)
        self.reset__default.setGeometry(QtCore.QRect(240, 370, 131, 29))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Reset_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset__default.setIcon(icon1)
        self.reset__default.setObjectName(_fromUtf8("reset__default"))
        self.label_title = QtGui.QLabel(self.tab)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 68, 17))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.change__image = QtGui.QPushButton(self.tab)
        self.change__image.setGeometry(QtCore.QRect(240, 250, 131, 29))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Plus_18px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change__image.setIcon(icon2)
        self.change__image.setIconSize(QtCore.QSize(18, 18))
        self.change__image.setObjectName(_fromUtf8("change__image"))
        self.delete__image = QtGui.QPushButton(self.tab)
        self.delete__image.setGeometry(QtCore.QRect(240, 330, 131, 29))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Delete_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete__image.setIcon(icon3)
        self.delete__image.setObjectName(_fromUtf8("delete__image"))
        self.authors = QtGui.QLineEdit(self.tab)
        self.authors.setGeometry(QtCore.QRect(20, 120, 351, 31))
        self.authors.setObjectName(_fromUtf8("authors"))
        self.label_author = QtGui.QLabel(self.tab)
        self.label_author.setGeometry(QtCore.QRect(20, 96, 71, 17))
        self.label_author.setObjectName(_fromUtf8("label_author"))
        self.title = QtGui.QLineEdit(self.tab)
        self.title.setGeometry(QtCore.QRect(20, 45, 351, 31))
        self.title.setObjectName(_fromUtf8("title"))
        self.from__category = QtGui.QComboBox(self.tab)
        self.from__category.setGeometry(QtCore.QRect(20, 190, 131, 31))
        self.from__category.setObjectName(_fromUtf8("from__category"))
        self.save = QtGui.QPushButton(self.tab)
        self.save.setGeometry(QtCore.QRect(280, 480, 91, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Plus_18px_White.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon4)
        self.save.setIconSize(QtCore.QSize(18, 18))
        self.save.setObjectName(_fromUtf8("save"))
        self.move_to = QtGui.QLabel(self.tab)
        self.move_to.setGeometry(QtCore.QRect(177, 197, 50, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.move_to.setFont(font)
        self.move_to.setObjectName(_fromUtf8("move_to"))
        self.to__category = QtGui.QComboBox(self.tab)
        self.to__category.setGeometry(QtCore.QRect(240, 190, 131, 31))
        self.to__category.setObjectName(_fromUtf8("to__category"))
        self.to__category.addItem(_fromUtf8(""))
        self.to__category.setItemText(0, _fromUtf8(""))
        self.book__image = QtGui.QLabel(self.tab)
        self.book__image.setGeometry(QtCore.QRect(20, 250, 161, 221))
        self.book__image.setStyleSheet(_fromUtf8(""))
        self.book__image.setText(_fromUtf8(""))
        self.book__image.setScaledContents(True)
        self.book__image.setObjectName(_fromUtf8("book__image"))
        self.get__image = QtGui.QPushButton(self.tab)
        self.get__image.setGeometry(QtCore.QRect(240, 290, 131, 29))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Download_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get__image.setIcon(icon5)
        self.get__image.setIconSize(QtCore.QSize(16, 16))
        self.get__image.setObjectName(_fromUtf8("get__image"))
        self.notice = QtGui.QLabel(self.tab)
        self.notice.setGeometry(QtCore.QRect(24, 153, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.notice.setFont(font)
        self.notice.setObjectName(_fromUtf8("notice"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Edit File_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.note = QtGui.QTextEdit(self.tab_2)
        self.note.setGeometry(QtCore.QRect(0, 0, 401, 531))
        self.note.setFrameShape(QtGui.QFrame.NoFrame)
        self.note.setObjectName(_fromUtf8("note"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Note_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon7, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit book", None))
        self.reset__default.setText(_translate("Dialog", "Reset default", None))
        self.label_title.setText(_translate("Dialog", "Title :", None))
        self.change__image.setText(_translate("Dialog", "Change image", None))
        self.delete__image.setText(_translate("Dialog", "Delete image", None))
        self.label_author.setText(_translate("Dialog", "Author(s) :", None))
        self.save.setText(_translate("Dialog", "Save", None))
        self.move_to.setText(_translate("Dialog", "Move to", None))
        self.get__image.setText(_translate("Dialog", "Get image", None))
        self.notice.setText(_translate("Dialog", "* separate authors by comma, example: Author1, Author2, etc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Note", None))

import ui.images_rc
