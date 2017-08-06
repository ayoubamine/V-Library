# -*- coding: utf-8 -*-

import PyQt4.QtGui as qt
from PyQt4.QtCore import (Qt, SIGNAL)
from ui.about import Ui_Dialog as Ui_Dialog_About
from ui.select_categories import Ui_Dialog as Ui_Dialog_Categories
from zipfile import ZipFile
from webbrowser import open_new
from os.path import expanduser
from py.threads import BackupThread
from py.threads import RestoreThread
from datetime import date
import os


class BackupRestore():
	
	def __init__(self, parent):

		self.parent = parent

	def loader(self):
		'''
		'''
		movie = qt.QMovie(':/interface/images/loader.gif', 'GIF')
		self.dialog.ui.loader.setMovie(movie)
		movie.start()
		self.dialog.ui.backup.setEnabled(False)
		self.dialog.ui.restore.setEnabled(False)

	def error(self):
		'''
		'''
		self.dialog.ui.loader.setPixmap(qt.QPixmap(':/interface/images/Delete_51px.png'))
		self.dialog.ui.backup.setEnabled(True)
		self.dialog.ui.restore.setEnabled(True)

	def success(self):
		'''
		'''
		self.dialog.ui.loader.setPixmap(qt.QPixmap(':/interface/images/Checkmark_51px.png'))
		self.dialog.ui.backup.setEnabled(True)
		self.dialog.ui.restore.setEnabled(True)

	def show(self):
		'''
		'''
		self.dialog = qt.QDialog()
		self.dialog.ui = Ui_Dialog_About()
		self.dialog.ui.setupUi(self.dialog)
		self.dialog.setWindowFlags(self.dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

		self.dialog.ui.license.clicked.connect(self.license)
		self.dialog.ui.github.mousePressEvent = self.github
		self.dialog.ui.email.mousePressEvent = self.clipboard
		self.dialog.ui.backup.clicked.connect(self.backup_dialog)
		self.dialog.ui.restore.clicked.connect(self.restore)

		self.dialog.exec_()

	def github(self, event):
		'''
			Open V-Library website
		'''
		open_new('v-library.github.io')

	def clipboard(self, event):
		'''
			Copy the email to clipboard
		'''
		myClipBoard = qt.QApplication.clipboard()
		myClipBoard.setText('programmer010011@gmail.com')

	def license(self):
		'''
			Read and show LICENSE file
		'''
		dialog = qt.QDialog(self.dialog)
		dialog.setFixedSize(500, 300)
		dialog.setWindowTitle("License")
		dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
		plain_text = qt.QPlainTextEdit(dialog)
		plain_text.resize(500, 300)
		plain_text.setReadOnly(True)

		with open(self.resource_path('LICENSE'), 'r') as file:
			plain_text.setPlainText(file.read())

		dialog.exec_()

	def resource_path(self, relative_path):
		'''
			Get absolute path to resource, works for dev and for PyInstaller
		'''
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath('.')

		return os.path.join(base_path, relative_path)

	def backup_dialog(self):
		'''
			Show all categories not empty in QListWidget
		'''
		categories = qt.QDialog(self.dialog)
		categories.ui = Ui_Dialog_Categories()
		categories.ui.setupUi(categories)
		categories.setWindowTitle("Backup")
		categories.setWindowFlags(categories.windowFlags() & ~Qt.WindowContextHelpButtonHint)

		categories.ui.go.clicked.connect(lambda: self.backup(categories))
		categories.ui.cancel.clicked.connect(categories.close)

		for i in range(self.parent.list__categories.count()):
			name = self.parent.list__categories.item(i).text()
			list_dir = os.listdir(self.parent.HOME_DIR + 'Data/' + name + '/books')
			
			if len(list_dir) > 0:
				item = qt.QListWidgetItem(name)
				item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
				item.setCheckState(Qt.Checked)
				categories.ui.categories.addItem(item)

		categories.exec_()

	def backup(self, dialog):
		'''
			Start backup thread
		'''
		# Get all items checked in QListWidget
		items_checked = []
		
		for i in range(dialog.ui.categories.count()):
			if dialog.ui.categories.item(i).checkState() == Qt.Checked:
				items_checked.append(dialog.ui.categories.item(i).text())

		if len(items_checked) > 0:
			
			backup_file = qt.QFileDialog.getSaveFileName(dialog, 'Backup directory', expanduser("~"), 'zip files (*.zip);;All Files (*)')

			if len(backup_file) > 0:
				today = date.today()
				name, ext = os.path.splitext(backup_file)
				name += ' ' + today.strftime("%d-%m-%Y")
				
				self.thread = BackupThread(name + ext, self.parent.HOME_DIR + 'Data', items_checked)
				self.parent.connect(self.thread, SIGNAL("finished()"), self.success)
				self.thread.start()

				dialog.close()
				self.loader()

	def restore_result(self, result, categories = None):
		'''
			Restore result SIGNAL
		'''
		if result:
			for category in categories:
				self.parent.rows += 1
				self.parent.db.add_category(category, self.parent.rows)
			self.parent.list__categories.clear()
			self.parent.list_categories.view_categories()
			
			self.success()
		else:
			self.error()

	def restore(self):
		'''
			Start restore thread
		'''
		restore_file = qt.QFileDialog.getOpenFileName(self.dialog, 'Restore file', expanduser("~"), 'Zip file (*.zip)')

		if len(restore_file) > 0:
			self.loader()
			self.thread = RestoreThread(self.parent.HOME_DIR, restore_file, self.parent.HOME_DIR + 'Temp/')
			self.thread.start()
			self.parent.connect(self.thread, SIGNAL('RESTORE'), self.restore_result)
