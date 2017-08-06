#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4.QtGui import (QApplication, QMainWindow, QDesktopWidget)
from ui.mainwindow import Ui_MainWindow

from os.path import expanduser
from sys import argv

from py.db import DB
from py.data_folder import DataFolder
from py.list_categories import ListCategories
from py.list_books import ListBooks
from py.backup_restore import BackupRestore
from py.alert import Alert


class Main(QMainWindow , Ui_MainWindow):
	def __init__(self, HOME_DIR, db, data_folder):
		
		QMainWindow.__init__(self)
		self.setupUi(self)

		self.HOME_DIR = HOME_DIR
		
		self.db = db
		self.data_folder = data_folder
		self.list_books = ListBooks(self)
		self.list_categories = ListCategories(self)
		self.backup_restore = BackupRestore(self)
		self.alert = Alert(self)

		# Getting number of rows in the database
		self.rows = len(self.db)

		# Center window in screen
		self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

		self.progressBar.hide()
		self.search__line__edit.hide()
		self.sidebar.hide()
		self.alert__form.hide()

		#########################[ connect ]#########################

		### list__categories
		self.list__categories.itemClicked.connect(self.list_categories.change_category)
		self.add__category.clicked.connect(self.list_categories.add_category)
		self.edit__category.clicked.connect(self.list_categories.edit_category)
		self.list__categories.itemDoubleClicked.connect(self.list_categories.edit_category)
		self.list__categories.model().layoutChanged.connect(self.list_categories.on_layout_change)

		### list books
		self.list__books.itemClicked.connect(self.list_books.change_book)
		self.add__book.clicked.connect(self.list_books.add_book)
		self.open__book.clicked.connect(self.list_books.open_book)
		self.list__books.itemDoubleClicked.connect(self.list_books.open_book)
		self.delete__book.clicked.connect(self.list_books.delete_book)
		self.edit__book.clicked.connect(self.list_books.edit_book)
		self.get__book.clicked.connect(self.list_books.get_book)
		self.slider.valueChanged.connect(self.list_books.slider_effect)
		self.list__mode.clicked.connect(self.list_books.list_mode)
		self.icon__mode.clicked.connect(self.list_books.icon_mode)
		self.toggle__sidebar.clicked.connect(self.list_books.toggle_sidebar)
		self.search.clicked.connect(self.list_books.toggle_search)
		self.search__line__edit.returnPressed.connect(self.list_books.search)
		
		### about - backup - restore
		self.about.clicked.connect(self.backup_restore.show)

		### alert
		self.close.clicked.connect(self.alert.hide)

		#########################[ connect ]#########################Python object

		self.list_categories.view_categories()
		self.list_books.slider_effect(145)

	def closeEvent(self, event):
		'''
			Accept/Ignore close event
		'''
		if self.progressBar.isVisible():
			self.alert.show('Ohh!!! wait, Adding books not finished.')
			# Ignore close
			event.ignore()
		else:
			# Accept close
			event.accept()



if __name__ == "__main__":
	# On Unix and Windows, return the argument with an initial component of ~ or ~user replaced by that user‘s home directory.
	HOME_DIR = expanduser("~/V-Library-Data/")
	# For portable version
	# HOME_DIR = os.path.dirname(os.path.realpath(__file__))
	# Create the QApplication
	app = QApplication(argv)
	data_folder = DataFolder(HOME_DIR)
	data_folder.create_folders()
	db = DB(HOME_DIR)
	#The Main window
	window = Main(HOME_DIR, db, data_folder)
	window.show()
	# Enter the main loop
	app.exec_()
	# Close the database connection
	db.close()
