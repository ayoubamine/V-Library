# -*- coding: utf-8 -*-

import PyQt4.QtGui as qt
from PyQt4.QtCore import (Qt, QSize, SIGNAL)
from ui.edit_book import Ui_Dialog as Ui_Dialog_Book
from py.threads import (AddBooksThread, ResetImage)
from os.path import expanduser
from wand.image import Image
from webbrowser import open_new
from json import (load, dump)
from glob import glob
import os


class ListBooks():

	def __init__(self, parent):

		self.parent = parent

	def image_book(self, image):
		'''
			Return image path if path refers to an existing path or return default path image
		'''
		if os.path.exists(image):
			return image
		return ':/interface/images/book.png'

	def category_selected(self):
		'''
			Return category of book selected
		'''
		if self.parent.list__categories.currentItem() is not None:
			return self.parent.list__categories.currentItem().text()

		if type(self.search_result[self.book_selected()]) is str:
			return self.search_result[self.book_selected()]

		index = 0
		for i in range(self.parent.list__books.count()):
			if self.parent.list__books.item(i) == self.parent.list__books.currentItem():
				break
			if self.parent.list__books.item(i).text() == self.parent.list__books.currentItem().text():
				index += 1

		print(index)

		return self.search_result[self.book_selected()][index]

	def book_selected(self):
		'''
			Return item selected in QListWidget
		'''
		return self.parent.list__books.currentItem().text()

	def path(self, category = None):
		'''
			Return home directory + category selected
		'''
		directory = self.parent.HOME_DIR + 'Data/'

		if category is None:
			directory += self.category_selected() + '/'
		else:
			directory += category + '/'
		
		return directory

	def book_path(self, option = None):
		'''
			Return path book selected in QListWidget
		'''
		if option == 'name':
			return self.book_selected()
		
		path = self.path() + 'books/' + self.book_selected() + '.*'
		file = glob(path)[0]

		if option == 'ext':
			# Split the file path into a pair (root, ext), and return ext
			return os.path.splitext(file)[1]

		return file

	def change_book(self, item):
		'''
			Save book name selected
		'''
		if self.parent.sidebar.isVisible():
			self.update_sidebar_info()

	def isvalid(self, name):
		'''
			Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
			A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
		'''
		if len(name) > 0:
			for c in name:
				if not (c.isalnum() or c in "_-'.() "):
					return False
			
			return True

		return False

	def add_book(self):
		'''
			Add books in the category selected.
		'''
		if self.parent.list__categories.currentItem() is not None:
			self.files = qt.QFileDialog.getOpenFileNames(self.parent, 'Add book', expanduser("~"), 'pdf files (*.pdf)')

			if len(self.files) > 0:
				directory = self.path()
				self.category = self.parent.list__categories.currentItem().text()
				
				if len(self.files) > 0:
					self.len_files = len(self.files)
					self.increment_value = 100 / self.len_files
					self.progress_bar_value = 0
					self.counter = 0
					self.parent.progressBar.setValue(0)
					self.parent.progressBar.show()
					self.parent.add__book.setEnabled(False)

					self.thread = AddBooksThread(self.files, directory, self.parent.HOME_DIR)
					self.thread.update.connect(self.progress_bar)
					self.thread.done.connect(self.backup_result)
					self.thread.start()
		else:
			self.parent.alert.show('Select a category before add books.')

	def progress_bar(self):
		'''
			Change progressBar value
		'''
		self.progress_bar_value += self.increment_value
		self.parent.progressBar.setValue(self.progress_bar_value)
		self.counter += 1

	def backup_result(self, files):
		'''
			View new books in QListWidget
		'''
		self.parent.progressBar.hide()
		self.parent.add__book.setEnabled(True)
		
		if self.category == self.parent.list__categories.currentItem().text():
			# Update GUI
			self.display_new_books(files)
			# Brush items in QListWidget
			self.brush(files)

	def brush(self, filenames):
		'''
			Brush items in QListWidget
		'''
		brush = qt.QBrush()
		brush.setColor(qt.QColor('#2B91AF'))
		for i in range(self.parent.list__books.count()):
			if self.parent.list__books.item(i).text() in filenames:
				self.parent.list__books.item(i).setForeground(brush)

	def display_books(self):
		'''
			Display all books in the category selected in QListWidget.
		'''
		self.parent.list__books.clear()

		path = self.path()

		for file in os.listdir(path + 'books/'):
			if os.path.isfile(path + 'books/' + file):
				item = qt.QListWidgetItem(os.path.splitext(file)[0])
				image = self.path() + 'images/' + os.path.splitext(file)[0] + '.png'
				item.setIcon(qt.QIcon(self.image_book(image)))
				self.parent.list__books.addItem(item)

	def display_new_books(self, files):
		'''
			Append new books in QListWidget.
		'''
		for file in files:
			item = qt.QListWidgetItem(file)
			image = self.path() + 'images/' + file + '.png'
			item.setIcon(qt.QIcon(self.image_book(image)))
			self.parent.list__books.addItem(item)

	def open_book(self):
		'''
			Open file with the default system program
		'''
		if self.parent.list__books.currentItem() is not None:
			open_new(self.book_path())

	def delete_book(self):
		'''
			Delete book from category selected
		'''
		if self.parent.list__books.currentItem() is not None:
			title = self.book_selected()
			book = self.book_path()
			image = self.path() + 'images/' + os.path.splitext(os.path.basename(book))[0] + '.png'
			data = self.path() + 'data/' + os.path.splitext(os.path.basename(book))[0] + '.txt'

			# Delete book, image and data from category folder
			self.parent.data_folder.delete_file(book)
			self.parent.data_folder.delete_file(data)
			
			if os.path.exists(image):
				self.parent.data_folder.delete_file(image)

			# Delete from GUI
			for i in range(self.parent.list__books.count()):
				if self.parent.list__books.item(i).text() == title:
					item = self.parent.list__books.takeItem(i)
					# Items removed from a list widget will not be managed by Qt, and will need to be deleted manually
					item = None
					break

			# Hide sidebar
			if self.parent.sidebar.isVisible():
				self.toggle_sidebar()

	def get_book(self):
		'''
			Copy book from category folder to another folder
		'''
		if self.parent.list__books.currentItem() is not None:
			directory = qt.QFileDialog.getExistingDirectory(self.parent, "Select Directory", expanduser("~"))

			if len(directory) > 0:
				self.parent.data_folder.copy_to(self.book_path(), directory)
				open_new(directory)

	def slider_effect(self, value):
		'''
			Change width and height items in QListWidget
		'''
		style_sheet = 'QListWidget#list__books:item{width: ' + str(value) + 'px;height: ' + str(value + 60) + 'px}'
		self.parent.list__books.setIconSize(QSize(value + 10, value + 10))
		self.parent.list__books.setStyleSheet(style_sheet)

	def list_mode(self):
		'''
			Change mode QListWidget
		'''
		self.parent.slider.setEnabled(False)

		self.parent.list__books.setViewMode(qt.QListView.ListMode)
		self.parent.list__books.setStyleSheet('QListWidget#list__books:item{height:50px;margin:0}')
		self.parent.list__books.setFlow(qt.QListView.TopToBottom)
		self.parent.list__books.setIconSize(QSize(50, 50))
		self.parent.list__books.setSpacing(4)

	def icon_mode(self):
		'''
			Change mode QListWidget
		'''
		self.parent.slider.setEnabled(True)

		self.parent.list__books.setViewMode(qt.QListView.IconMode)
		self.parent.list__books.setFlow(qt.QListView.LeftToRight)
		self.slider_effect(self.parent.slider.value())
		self.parent.list__books.setSpacing(0)

	def toggle_sidebar(self):
		'''
			Toggle sidebar
		'''
		if self.parent.sidebar.isVisible():
			self.parent.toggle__sidebar.setIcon(qt.QIcon(':/interface/images/Left page_24px.png'))
			self.parent.toggle__sidebar.setToolTip('Show')
			self.parent.sidebar.hide()
		
		elif self.parent.list__books.currentItem() is not None:
			self.parent.toggle__sidebar.setIcon(qt.QIcon(':/interface/images/Right page_24px.png'))
			self.parent.toggle__sidebar.setStyleSheet('QToolButton{padding:3px}')
			self.parent.toggle__sidebar.setToolTip('Hide')
			self.parent.sidebar.show()
			self.update_sidebar_info()

	def update_sidebar_info(self):
		'''
			Update sidebar info
		'''
		title = self.book_selected()
		category = self.category_selected()
		directory = self.path(category)
		
		self.parent.book__title.setText(title)
		self.parent.book__image.setPixmap(qt.QPixmap(self.image_book(directory + 'images/' + title + '.png')))
		self.parent.book__category.setText(category)

		with open(directory + 'data/' + title + '.txt', 'r') as outfile:
			# JSON document to a Python object
			data = load(outfile)

		if 'pages' in data:
			self.parent.book__pages.setText(str(data['pages']))
			self.parent.book__pages.show()
			self.parent.book__pages__lbl.show()
		else:
			self.parent.book__pages.hide()
			self.parent.book__pages__lbl.hide()

		if 'authors' in data:
			self.parent.book__author.setText(data['authors'])
			self.parent.book__author.show()
			self.parent.book__author__lbl.show()
		else:
			self.parent.book__author.hide()
			self.parent.book__author__lbl.hide()

	def toggle_search(self):
		'''
			Toggle search
		'''
		if self.parent.search__line__edit.isVisible():
			self.parent.search__line__edit.hide()
		else:
			self.parent.search__line__edit.show()

	def search(self):
		'''
			Search book and view in QListWidget
		'''
		self.parent.list__books.clear()

		# Clearing selection in QListWidget
		self.parent.list__categories.selectionModel().clear()

		value = self.parent.search__line__edit.text().lower()
		directory = self.parent.HOME_DIR + 'Data/'
		categories = os.listdir(directory)
		# Save search result
		self.search_result = {}

		for category in categories:
			for file in os.listdir(directory + category + '/books'):
				if os.path.isfile(directory + category + '/books/' + file):
					# Get filename from pathname
					filename = os.path.splitext(os.path.basename(file))[0]
					if value in filename.lower():
						if filename in self.search_result:
							if type(self.search_result[filename]) is str:
								self.search_result[filename] = (self.search_result[filename], category)
							else:
								self.search_result[filename] += (category,)
						else:
							self.search_result[filename] = category
						item = qt.QListWidgetItem(filename)
						item.setIcon(qt.QIcon(self.image_book(directory + category + '/images/' + filename + '.png')))
						self.parent.list__books.addItem(item)

		print(self.search_result)

	def edit_book(self):
		'''
			Edit information book
		'''
		if self.parent.list__books.currentItem() is not None:
			
			self.dialog = qt.QDialog(self.parent)
			self.dialog.ui = Ui_Dialog_Book()
			self.dialog.ui.setupUi(self.dialog)
			self.dialog.setWindowFlags(self.dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

			title = self.book_selected()
			directory = self.path()
			book_image = os.path.splitext(directory)[0] + 'images/' + title + '.png'
			authors = ''
			note = ''

			self.dialog.ui.title.setText(title)
			self.dialog.ui.book__image.setPixmap(qt.QPixmap(self.image_book(book_image)))

			# Get information book from text file
			with open(directory + 'data/' + title + '.txt', 'r') as outfile:
				# JSON document to a Python object
				data = load(outfile)

			if 'authors' in data:
				self.dialog.ui.authors.setText(data['authors'])
				authors = data['authors']

			if 'note' in data:
				self.dialog.ui.note.setText(data['note'])
				note = data['note']

			# Add categories names in QComboBox
			category = self.category_selected()
			self.dialog.ui.from__category.addItem(category)
			
			for i in range(self.parent.list__categories.count()):
				if category != self.parent.list__categories.item(i).text():
					self.dialog.ui.to__category.addItem(self.parent.list__categories.item(i).text())

			self.dialog.ui.change__image.clicked.connect(self.change_image)
			self.dialog.ui.get__image.clicked.connect(self.get_image)
			self.dialog.ui.delete__image.clicked.connect(self.delete_image)
			self.dialog.ui.reset__default.clicked.connect(self.reset_default)
			self.dialog.ui.save.clicked.connect(lambda: self.save(title, authors, note))

			self.dialog.exec_()

	def reset_result(self, path = None):
		'''
			Reset result SIGNAL
		'''
		if path is not None:
			# Update GUI
			self.dialog.ui.book__image.setPixmap(qt.QPixmap(path))
			self.parent.list__books.currentItem().setIcon(qt.QIcon(path))
		
		self.dialog.ui.reset__default.setEnabled(True)

	def reset_default(self):
		'''
			Start reset book image thread
		'''
		self.dialog.ui.reset__default.setEnabled(False)
		
		path = self.path() + 'images/' + self.book_selected() + '.png'
		book_path = self.book_path()
		
		self.thread = ResetImage(self.parent.HOME_DIR, path, book_path)
		self.parent.connect(self.thread, SIGNAL('END'), self.reset_result)
		self.thread.start()

	def change_image(self):
		'''
			Change book image
		'''
		image = qt.QFileDialog.getOpenFileName(self.dialog, 'Find Picture', expanduser("~"), 'Picture (*.png *.jpeg *.jpg)')

		if len(image) > 0:
			path = self.path() + 'images/' + self.book_selected() + '.png'
			
			if image.endswith('.png'):
				self.parent.data_folder.copy_to(image, path)
			else:
				with Image(filename = image) as img:
					img.save(filename = path)

			# Update GUI
			self.dialog.ui.book__image.setPixmap(qt.QPixmap(path))
			self.parent.list__books.currentItem().setIcon(qt.QIcon(path))

	def get_image(self):
		'''
			Copy book image from category folder to another folder
		'''
		if os.path.exists(self.path() + 'images/' + self.book_selected() + '.png'):
			directory = qt.QFileDialog.getExistingDirectory(self.dialog, "Select Directory", expanduser("~"))

			if len(directory) > 0:
				self.parent.data_folder.copy_to(self.path() + 'images/' + self.book_selected() + '.png', directory)
				open_new(directory)

	def delete_image(self):
		'''
			Delete book image and set default
		'''
		if os.path.exists(self.path() + 'images/' + self.book_selected() + '.png'):
			self.parent.data_folder.delete_file(self.path() + 'images/' + self.book_selected() + '.png')
			self.dialog.ui.book__image.setPixmap(qt.QPixmap(':/interface/images/book.png'))
			self.parent.list__books.currentItem().setIcon(qt.QIcon(':/interface/images/book.png'))

	def save(self, old_title, old_authors, old_note):
		'''
			Save all modifications
		'''
		title = self.dialog.ui.title.text().strip()
		authors = self.dialog.ui.authors.text()
		note = self.dialog.ui.note.toPlainText()

		if title != old_title:
			if self.isvalid(title):
				directory = self.path()
				name = self.book_path('name')
				ext = self.book_path('ext')
				generate = self.parent.data_folder.generate_book_name(directory + 'books/' + title + ext)
				name = os.path.splitext(generate)[0]
				
				self.parent.data_folder.rename(directory + 'books', old_title + ext, name + ext)
				self.parent.data_folder.rename(directory + 'data', old_title + '.txt', name + '.txt')
				if os.path.exists(directory + 'images/' + old_title + '.png'):
					self.parent.data_folder.rename(directory + 'images', old_title + '.png', name + '.png')

				# Update GUI
				self.parent.list__books.currentItem().setText(name)
			else:
				self.parent.alert.show('The book name is not valid.')

		if note != old_note:
			with open(self.path() + 'data/' + old_title + '.txt', 'r+') as outfile:
				# Python object to JSON document
				data = load(outfile)
				data['note'] = note
				# Move the cursor back to the beginning of the file
				outfile.seek(0)
				# Start writing
				dump(data, outfile)
				# truncate() to deal with the case where the new data is smaller than the previous
				outfile.truncate()

		if authors != old_authors:
			authors_split = [author.strip() for author in authors.split(',')]

			with open(self.path() + 'data/' + self.book_selected() + '.txt', 'r+') as outfile:
				# Python object to JSON document
				data = load(outfile)
				data['authors'] = ', '.join(authors_split)
				# Move the cursor back to the beginning of the file
				outfile.seek(0)
				# Start writing
				dump(data, outfile)
				# truncate() to deal with the case where the new data is smaller than the previous
				outfile.truncate()

		if self.dialog.ui.to__category.currentText() != '':
			path = self.path()
			category = self.dialog.ui.to__category.currentText()

			name = self.book_path('name')
			ext = self.book_path('ext')
			
			generate = self.parent.data_folder.generate_book_name(self.path(category) + 'books/' + name + ext)
			filename = os.path.basename(generate)
			name_grt = os.path.splitext(filename)[0]

			# Move book + image + data to the new category selected
			self.parent.data_folder.move_to(path + 'books/' + name + ext, self.path(category) + 'books/' + name_grt + ext)
			self.parent.data_folder.move_to(path + 'data/' + name + '.txt', self.path(category) + 'data/' + name_grt + '.txt')
			if os.path.exists(path + 'images/' + name + '.png'):
				self.parent.data_folder.move_to(path + 'images/' + name + '.png', self.path(category) + 'images/' + name_grt + '.png')
		
			# Delete from GUI
			for i in range(self.parent.list__books.count()):
				if self.parent.list__books.item(i).text() == name:
					item = self.parent.list__books.takeItem(i)
					# Items removed from a list widget will not be managed by Qt, and will need to be deleted manually
					item = None
					break
		
		self.dialog.close()
