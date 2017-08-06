# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(870, 530)
        MainWindow.setMinimumSize(QtCore.QSize(870, 530))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("/*\n"
"    QMainWindow\n"
"*/\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"/*\n"
"    QListWidget\n"
"*/\n"
"\n"
"QListWidget#list__categories\n"
"{\n"
"    color:#607D8B;\n"
"    background-color: white;\n"
"    border-top: 0px;\n"
"}\n"
"QListWidget#list__categories:item\n"
"{\n"
"    background-color: #ECEFF1;\n"
"    margin-bottom:1px;\n"
"    padding:5px;\n"
"    height: 30px;\n"
"    border-radius: 0px\n"
"}\n"
"QListWidget#list__categories:item:hover\n"
"{\n"
"    background-color: #f2f2f2;\n"
"    border: 0px\n"
"}\n"
"QListWidget#list__categories:item:selected\n"
"{\n"
"    background-color: #f2f2f2;\n"
"    color:#607D8B;\n"
"}\n"
"\n"
"/*************************************/\n"
"\n"
"QListWidget#list__books\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    border-left: 0;\n"
"    border-right: 0;\n"
"    color: #607D8B;\n"
"    background-color: qlineargradient(spread:pad, x1:0.349, y1:0.869, x2:0.283,         y2:0.744, stop:0 rgba(250, 250, 250, 255), stop:0.330189 rgba(250, 250, 250, 255), stop:0.334906 rgba(250, 250, 250, 255), stop:0.665094 rgba(250, 250, 250, 255), stop:0.67 rgba(244, 244, 244, 255), stop:1 rgba(244, 244, 244, 255))\n"
"}\n"
"\n"
"QListWidget#list__books:item\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    margin: 8px;\n"
"    width: 129px;\n"
"    height: 190px\n"
"}\n"
"\n"
"QListWidget#list__books:item:hover\n"
"{\n"
"    background-color: #f2f2f2;\n"
"    border: 1px solid #ECEFF1\n"
"}\n"
"\n"
"QListWidget#list__books:item:selected\n"
"{\n"
"    background-color: #f2f2f2;\n"
"    border: 1px solid #ECEFF1;\n"
"    color: #607D8B\n"
"}\n"
"\n"
"/*\n"
"    QFrame\n"
"*/\n"
"\n"
"QFrame#sidebar\n"
"{\n"
"    background-color: white;\n"
"    border: 1px solid #f2f2f2\n"
"}\n"
"\n"
"QFrame#alert__form\n"
"{\n"
"    background-color: #4687D6;\n"
"    border: 0\n"
"}\n"
"\n"
"/*\n"
"    QLineEdit\n"
"*/\n"
"\n"
"QLineEdit#name__category,\n"
"QLineEdit#search__line__edit\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    color: #607D8B;\n"
"    height: 34px;\n"
"    padding: 0 5px\n"
"}\n"
"\n"
"QLineEdit#search__line__edit\n"
"{\n"
"    width: 200px;\n"
"    height: 32px\n"
"}\n"
"\n"
"/*\n"
"    QToolButton\n"
"*/\n"
"\n"
"QToolButton\n"
"{\n"
"    background: transparent;\n"
"    width: 30px;\n"
"    padding: 4px;\n"
"    border: 0\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: #ECEFF1;\n"
"    border-radius: 3px\n"
"}\n"
"\n"
"QToolButton#add__category,\n"
"QToolButton#edit__category\n"
"{\n"
"    border: 1px solid #f2f2f2;\n"
"    border-right: 0;\n"
"    width: 28px;\n"
"    height: 31px;\n"
"    padding: 0px;\n"
"    border-radius: 0\n"
"}\n"
"\n"
"QToolButton#add__category\n"
"{\n"
"    border-right: 0;\n"
"    border-left: 0\n"
"}\n"
"\n"
"QToolButton#close:hover\n"
"{\n"
"    background-color: none\n"
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
"}\n"
"\n"
"/*\n"
"    QProgressBar\n"
"*/\n"
"\n"
"QProgressBar\n"
"{\n"
"    border-radius: 0;\n"
"    background-color: #c0d4ea\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #5294e2\n"
"}\n"
"\n"
"/*\n"
"    QToolTip\n"
"*/\n"
"\n"
"QToolTip\n"
"{\n"
"    color: grey;\n"
"    border: 0;\n"
"    background-color: white\n"
"}\n"
"\n"
"/*\n"
"    QMain\n"
"*/\n"
"\n"
"QMain\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
"    QMenu\n"
"*/\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 4px 20px 4px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"     background: #4c7fbf;\n"
"     color:white\n"
"}\n"
"\n"
"/*\n"
"    QLabel\n"
"*/\n"
"\n"
"QLabel\n"
"{\n"
"    color: grey\n"
"}\n"
"\n"
"QLabel#book__image\n"
"{\n"
"    border: 0px\n"
"}\n"
"\n"
"QLabel#book__title\n"
"{\n"
"    margin-bottom: 20px\n"
"}\n"
"\n"
"QLabel#book__title,\n"
"QLabel#book__author,\n"
"QLabel#book__category\n"
"{\n"
"    color: #5c616c\n"
"}\n"
"\n"
"QLabel#msg\n"
"{\n"
"    color: white\n"
"}\n"
"\n"
"/*\n"
"    QSlider\n"
"*/\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    background: white;\n"
"    height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"    background: #5294e2;\n"
"    border: 1px solid #c9def6;\n"
"    height: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal\n"
"{\n"
"    background: #cfd6e6;\n"
"    border: 1px solid #f0f2f7;\n"
"    height: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background: white;\n"
"    border: 1px solid #cfd6e6;\n"
"    width: 13px;\n"
"    margin-top: -5px;\n"
"    margin-bottom: -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover\n"
"{\n"
"    background: #5294e2;\n"
"    border: 1px solid #5294e2;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled\n"
"{\n"
"    border: 1px solid #f0f2f7;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 8, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(8, 2, 8, 2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add__book = QtGui.QToolButton(self.centralwidget)
        self.add__book.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Add File_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add__book.setIcon(icon1)
        self.add__book.setIconSize(QtCore.QSize(26, 26))
        self.add__book.setObjectName(_fromUtf8("add__book"))
        self.horizontalLayout.addWidget(self.add__book)
        self.open__book = QtGui.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/View_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open__book.setIcon(icon2)
        self.open__book.setIconSize(QtCore.QSize(26, 26))
        self.open__book.setObjectName(_fromUtf8("open__book"))
        self.horizontalLayout.addWidget(self.open__book)
        self.edit__book = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Edit File_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit__book.setIcon(icon3)
        self.edit__book.setIconSize(QtCore.QSize(26, 26))
        self.edit__book.setObjectName(_fromUtf8("edit__book"))
        self.horizontalLayout.addWidget(self.edit__book)
        self.get__book = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Load Resume Template_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get__book.setIcon(icon4)
        self.get__book.setIconSize(QtCore.QSize(26, 26))
        self.get__book.setObjectName(_fromUtf8("get__book"))
        self.horizontalLayout.addWidget(self.get__book)
        self.delete__book = QtGui.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Delete File_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete__book.setIcon(icon5)
        self.delete__book.setIconSize(QtCore.QSize(26, 26))
        self.delete__book.setObjectName(_fromUtf8("delete__book"))
        self.horizontalLayout.addWidget(self.delete__book)
        self.about = QtGui.QToolButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/About_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon6)
        self.about.setIconSize(QtCore.QSize(26, 26))
        self.about.setObjectName(_fromUtf8("about"))
        self.horizontalLayout.addWidget(self.about)
        spacerItem = QtGui.QSpacerItem(285, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.search__line__edit = QtGui.QLineEdit(self.centralwidget)
        self.search__line__edit.setEnabled(True)
        self.search__line__edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.search__line__edit.setFont(font)
        self.search__line__edit.setDragEnabled(False)
        self.search__line__edit.setObjectName(_fromUtf8("search__line__edit"))
        self.horizontalLayout.addWidget(self.search__line__edit)
        self.search = QtGui.QToolButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Search_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon7)
        self.search.setIconSize(QtCore.QSize(26, 26))
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.list__mode = QtGui.QToolButton(self.centralwidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/News Feed_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.list__mode.setIcon(icon8)
        self.list__mode.setIconSize(QtCore.QSize(26, 26))
        self.list__mode.setObjectName(_fromUtf8("list__mode"))
        self.horizontalLayout.addWidget(self.list__mode)
        self.icon__mode = QtGui.QToolButton(self.centralwidget)
        self.icon__mode.setStyleSheet(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Grid View_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon__mode.setIcon(icon9)
        self.icon__mode.setIconSize(QtCore.QSize(26, 26))
        self.icon__mode.setChecked(False)
        self.icon__mode.setObjectName(_fromUtf8("icon__mode"))
        self.horizontalLayout.addWidget(self.icon__mode)
        self.toggle__sidebar = QtGui.QToolButton(self.centralwidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Left page_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle__sidebar.setIcon(icon10)
        self.toggle__sidebar.setIconSize(QtCore.QSize(26, 26))
        self.toggle__sidebar.setObjectName(_fromUtf8("toggle__sidebar"))
        self.horizontalLayout.addWidget(self.toggle__sidebar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.name__category = QtGui.QLineEdit(self.centralwidget)
        self.name__category.setMaximumSize(QtCore.QSize(185, 16777215))
        self.name__category.setStyleSheet(_fromUtf8(""))
        self.name__category.setInputMask(_fromUtf8(""))
        self.name__category.setText(_fromUtf8(""))
        self.name__category.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.name__category.setObjectName(_fromUtf8("name__category"))
        self.horizontalLayout_2.addWidget(self.name__category)
        self.add__category = QtGui.QToolButton(self.centralwidget)
        self.add__category.setStyleSheet(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Plus_18px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add__category.setIcon(icon11)
        self.add__category.setIconSize(QtCore.QSize(18, 18))
        self.add__category.setObjectName(_fromUtf8("add__category"))
        self.horizontalLayout_2.addWidget(self.add__category)
        self.edit__category = QtGui.QToolButton(self.centralwidget)
        self.edit__category.setEnabled(True)
        self.edit__category.setStyleSheet(_fromUtf8("border-right: 0"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Edit_16px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit__category.setIcon(icon12)
        self.edit__category.setIconSize(QtCore.QSize(16, 16))
        self.edit__category.setObjectName(_fromUtf8("edit__category"))
        self.horizontalLayout_2.addWidget(self.edit__category)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list__categories = QtGui.QListWidget(self.centralwidget)
        self.list__categories.setMaximumSize(QtCore.QSize(250, 16777215))
        self.list__categories.setStyleSheet(_fromUtf8(""))
        self.list__categories.setFrameShape(QtGui.QFrame.NoFrame)
        self.list__categories.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.list__categories.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.list__categories.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.list__categories.setIconSize(QtCore.QSize(22, 22))
        self.list__categories.setObjectName(_fromUtf8("list__categories"))
        self.verticalLayout.addWidget(self.list__categories)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.alert__form = QtGui.QFrame(self.centralwidget)
        self.alert__form.setMinimumSize(QtCore.QSize(0, 37))
        self.alert__form.setStyleSheet(_fromUtf8(""))
        self.alert__form.setFrameShape(QtGui.QFrame.StyledPanel)
        self.alert__form.setFrameShadow(QtGui.QFrame.Raised)
        self.alert__form.setObjectName(_fromUtf8("alert__form"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.alert__form)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.msg = QtGui.QLabel(self.alert__form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.msg.setFont(font)
        self.msg.setText(_fromUtf8(""))
        self.msg.setObjectName(_fromUtf8("msg"))
        self.horizontalLayout_6.addWidget(self.msg)
        self.close = QtGui.QToolButton(self.alert__form)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/interface/images/Close_24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon13)
        self.close.setObjectName(_fromUtf8("close"))
        self.horizontalLayout_6.addWidget(self.close)
        self.verticalLayout_2.addWidget(self.alert__form)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 30)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.list__books = QtGui.QListWidget(self.centralwidget)
        self.list__books.setStyleSheet(_fromUtf8(""))
        self.list__books.setFrameShape(QtGui.QFrame.StyledPanel)
        self.list__books.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.list__books.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list__books.setAutoScroll(True)
        self.list__books.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.list__books.setAlternatingRowColors(False)
        self.list__books.setIconSize(QtCore.QSize(140, 140))
        self.list__books.setMovement(QtGui.QListView.Static)
        self.list__books.setFlow(QtGui.QListView.LeftToRight)
        self.list__books.setResizeMode(QtGui.QListView.Adjust)
        self.list__books.setLayoutMode(QtGui.QListView.SinglePass)
        self.list__books.setViewMode(QtGui.QListView.IconMode)
        self.list__books.setModelColumn(0)
        self.list__books.setUniformItemSizes(False)
        self.list__books.setWordWrap(True)
        self.list__books.setObjectName(_fromUtf8("list__books"))
        self.gridLayout_2.addWidget(self.list__books, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.sidebar = QtGui.QFrame(self.centralwidget)
        self.sidebar.setStyleSheet(_fromUtf8(""))
        self.sidebar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtGui.QFrame.Raised)
        self.sidebar.setObjectName(_fromUtf8("sidebar"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.sidebar)
        self.verticalLayout_4.setMargin(2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setMargin(5)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.book__image = QtGui.QLabel(self.sidebar)
        self.book__image.setMaximumSize(QtCore.QSize(151, 220))
        self.book__image.setStyleSheet(_fromUtf8(""))
        self.book__image.setText(_fromUtf8(""))
        self.book__image.setScaledContents(True)
        self.book__image.setObjectName(_fromUtf8("book__image"))
        self.gridLayout_3.addWidget(self.book__image, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.sidebar)
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: white;\n"
"border: 0px;"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 126, 366))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.book__title = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__title.setStyleSheet(_fromUtf8(""))
        self.book__title.setText(_fromUtf8(""))
        self.book__title.setWordWrap(True)
        self.book__title.setObjectName(_fromUtf8("book__title"))
        self.verticalLayout_5.addWidget(self.book__title)
        self.book__author__lbl = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__author__lbl.setMaximumSize(QtCore.QSize(16777215, 17))
        self.book__author__lbl.setObjectName(_fromUtf8("book__author__lbl"))
        self.verticalLayout_5.addWidget(self.book__author__lbl)
        self.book__author = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__author.setStyleSheet(_fromUtf8(""))
        self.book__author.setText(_fromUtf8(""))
        self.book__author.setWordWrap(True)
        self.book__author.setObjectName(_fromUtf8("book__author"))
        self.verticalLayout_5.addWidget(self.book__author)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.book__category = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__category.setStyleSheet(_fromUtf8(""))
        self.book__category.setText(_fromUtf8(""))
        self.book__category.setWordWrap(True)
        self.book__category.setObjectName(_fromUtf8("book__category"))
        self.verticalLayout_5.addWidget(self.book__category)
        self.book__pages__lbl = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__pages__lbl.setObjectName(_fromUtf8("book__pages__lbl"))
        self.verticalLayout_5.addWidget(self.book__pages__lbl)
        self.book__pages = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.book__pages.setText(_fromUtf8(""))
        self.book__pages.setObjectName(_fromUtf8("book__pages"))
        self.verticalLayout_5.addWidget(self.book__pages)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_5.setStretch(7, 6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addWidget(self.sidebar)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 5, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.slider = QtGui.QSlider(self.centralwidget)
        self.slider.setStyleSheet(_fromUtf8(""))
        self.slider.setMinimum(129)
        self.slider.setMaximum(190)
        self.slider.setProperty("value", 145)
        self.slider.setTracking(True)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.horizontalLayout_5.addWidget(self.slider)
        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.slider, self.edit__category)
        MainWindow.setTabOrder(self.edit__category, self.add__category)
        MainWindow.setTabOrder(self.add__category, self.name__category)
        MainWindow.setTabOrder(self.name__category, self.list__categories)
        MainWindow.setTabOrder(self.list__categories, self.add__book)
        MainWindow.setTabOrder(self.add__book, self.open__book)
        MainWindow.setTabOrder(self.open__book, self.edit__book)
        MainWindow.setTabOrder(self.edit__book, self.delete__book)
        MainWindow.setTabOrder(self.delete__book, self.about)
        MainWindow.setTabOrder(self.about, self.search__line__edit)
        MainWindow.setTabOrder(self.search__line__edit, self.search)
        MainWindow.setTabOrder(self.search, self.list__mode)
        MainWindow.setTabOrder(self.list__mode, self.icon__mode)
        MainWindow.setTabOrder(self.icon__mode, self.toggle__sidebar)
        MainWindow.setTabOrder(self.toggle__sidebar, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.list__books)
        MainWindow.setTabOrder(self.list__books, self.get__book)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "V-Library", None))
        self.add__book.setToolTip(_translate("MainWindow", "Add", None))
        self.add__book.setText(_translate("MainWindow", "...", None))
        self.open__book.setToolTip(_translate("MainWindow", "View", None))
        self.open__book.setText(_translate("MainWindow", "...", None))
        self.edit__book.setToolTip(_translate("MainWindow", "Edit", None))
        self.edit__book.setText(_translate("MainWindow", "...", None))
        self.get__book.setToolTip(_translate("MainWindow", "Copy book to...", None))
        self.get__book.setText(_translate("MainWindow", "...", None))
        self.delete__book.setToolTip(_translate("MainWindow", "Delete", None))
        self.delete__book.setText(_translate("MainWindow", "...", None))
        self.about.setToolTip(_translate("MainWindow", "About", None))
        self.about.setText(_translate("MainWindow", "...", None))
        self.search__line__edit.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.search.setToolTip(_translate("MainWindow", "Search", None))
        self.search.setText(_translate("MainWindow", "...", None))
        self.list__mode.setToolTip(_translate("MainWindow", "ListMode", None))
        self.list__mode.setText(_translate("MainWindow", "...", None))
        self.icon__mode.setToolTip(_translate("MainWindow", "IconMode", None))
        self.icon__mode.setText(_translate("MainWindow", "...", None))
        self.toggle__sidebar.setToolTip(_translate("MainWindow", "Show Panel", None))
        self.toggle__sidebar.setText(_translate("MainWindow", "...", None))
        self.name__category.setToolTip(_translate("MainWindow", "Add new category", None))
        self.name__category.setPlaceholderText(_translate("MainWindow", "Add new category", None))
        self.add__category.setToolTip(_translate("MainWindow", "Add", None))
        self.add__category.setText(_translate("MainWindow", "...", None))
        self.edit__category.setToolTip(_translate("MainWindow", "Edit", None))
        self.edit__category.setText(_translate("MainWindow", "...", None))
        self.book__author__lbl.setText(_translate("MainWindow", "Authors:", None))
        self.label_6.setText(_translate("MainWindow", "Category:", None))
        self.book__pages__lbl.setText(_translate("MainWindow", "Pages:", None))

import ui.images_rc
