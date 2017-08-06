# -*- coding: utf-8 -*-

import PyQt4.QtGui as qt
from PyQt4.QtCore import Qt
from ui.edit_category import Ui_Dialog as Ui_Dialog_Category
from os.path import expanduser
from glob import glob
import os


class ListCategories():

	def __init__(self, parent):

		self.parent = parent
		# Return the value of the named attribute of object
		self.path = getattr(self.parent.list_books, 'path')
		self.isvalid = getattr(self.parent.list_books, 'isvalid')

	def get_first(self, list_files):
		'''
			Return first element from list_files.
		'''
		if len(list_files) > 0:
			return list_files[0]
		return ''

	def category_selected(self):
		'''
			Return category selected in QListWidget
		'''
		return self.parent.list__categories.currentItem().text()

	def view_categories(self):
		'''
			Select all categories in database and add in QListWidget.
		'''
		data = self.parent.db.all_categories()

		for tup in data:
			item = qt.QListWidgetItem(tup[0])
			image = self.path(tup[0]) + tup[0] + '.*'
			item.setToolTip(tup[0])
			item.setIcon(qt.QIcon(self.get_first(glob(image))))
			self.parent.list__categories.addItem(item)

	def add_in_top(self, name):
		'''
			Insert item in top of the QListWidget
		'''
		item = qt.QListWidgetItem(name)
		item.setToolTip(name)
		# Add the QListWidgetItem in top of the QListWidget
		self.parent.list__categories.insertItem(0, item)

	def add_category(self):
		'''
			Add new category
		'''
		# Get category name form the GUI
		name = self.parent.name__category.text().strip()
		
		# Check the category name is valid and not duplicated in the database
		if self.isvalid(name):
			if self.parent.db.search_by_name(name):
				# Increment number of categories
				self.parent.rows += 1
				# Add category name in the database
				self.parent.db.add_category(name, self.parent.rows)
				# Create a folder for the new category
				self.parent.data_folder.add_folder(self.path(name))
				self.parent.data_folder.add_folder(self.path(name) + 'books')
				self.parent.data_folder.add_folder(self.path(name) + 'images')
				self.parent.data_folder.add_folder(self.path(name) + 'data')
				# Add the category name in the GUI
				self.add_in_top(name)
				# Clears the contents of the line edit
				self.parent.name__category.clear()
			else:
				self.parent.alert.show('The category name is duplicated.')
		else:
			self.parent.alert.show('The category name is not valid.')

	def on_layout_change(self):
		'''
			Save change order items after changed in GUI
		'''
		# Get all categories names from the GUI
		items = ()
		for item in range(self.parent.list__categories.count()-1, -1, -1):
			items += (self.parent.list__categories.item(item).text(),)

		# Reorder categories
		for sort, name in enumerate(items, 1):
			self.parent.db.reorder_categories(sort, name)

	def change_category(self, item):
		'''
			Save category name selected and enabled edit button
		'''
		# Display all books in the category selected in QListWidget
		self.parent.list_books.display_books()

	def edit_category(self):
		'''
			Edit/Delete category
		'''
		if self.parent.list__categories.currentItem() is not None:
			self.dialog = qt.QDialog(self.parent)
			self.dialog.ui = Ui_Dialog_Category()
			self.dialog.ui.setupUi(self.dialog)
			self.dialog.setWindowFlags(self.dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

			category = self.category_selected()
			self.dialog.ui.category__name.setText(category)
			pixmap = self.get_first(glob(self.path() + category + '.*'))
			self.dialog.ui.display__image.setPixmap(qt.QPixmap(pixmap))

			self.dialog.ui.save__info.clicked.connect(self.save_info)
			self.dialog.ui.delete__category.clicked.connect(self.delete_category)
			self.dialog.ui.delete__image.clicked.connect(self.delete_image)
			self.dialog.ui.set__image.clicked.connect(self.set_image)

			self.dialog.exec_()
		else:
			self.parent.alert.show('Select a category before editing.')

	def delete_category(self):
		'''
			Delete category with all inside content
		'''
		category = self.category_selected()
		
		# Delete category row from database
		self.parent.db.delete_category(category)

		# Delete a directory and all its contents
		self.parent.data_folder.delete_folder(self.path())

		# Delete from GUI
		for i in range(self.parent.list__categories.count()):
			if self.parent.list__categories.item(i).text() == category:
				item = self.parent.list__categories.takeItem(i)
				# Items removed from a list widget will not be managed by Qt, and will need to be deleted manually
				item = None
				del item
				break

		# Solve the problem of sorting in QListWidget when delete a item
		self.on_layout_change()
		
		self.parent.rows -= 1
		self.parent.list_books.toggle_sidebar()
		self.parent.list__books.clear()
		
		self.dialog.close()

	def save_info(self):
		'''
			Update category name
		'''
		old_text = self.category_selected()
		new_text = self.dialog.ui.category__name.text()

		if old_text != new_text:
			if self.isvalid(new_text):
				# Update database
				self.parent.db.update_category(old_text, new_text)

				# Update GUI
				items = self.parent.list__categories.findItems(old_text, Qt.MatchExactly)
				items[0].setText(new_text)

				# Update folder name
				self.parent.data_folder.rename(self.parent.HOME_DIR + 'Data', old_text, new_text)

				# Update category image name
				file = self.get_first(glob(self.path(new_text) + old_text + '.*'))

				if os.path.exists(file):
					dirname = os.path.dirname(file)
					name, ext = os.path.splitext(file)
					self.parent.data_folder.rename(dirname, old_text + ext, new_text + ext)
			else:
				self.parent.alert.show('The category name is not valid.')

		self.dialog.close()

	def delete_image(self):
		'''
			Delete image category from <img_cat> folder
		'''
		category = self.category_selected()
		pixmap = self.get_first(glob(self.path() + category + '.*'))
		
		# Return True if path refers to an existing path
		if os.path.exists(pixmap):
			self.parent.data_folder.delete_file(pixmap)
			self.dialog.ui.display__image.clear()

			# Delete from GUI
			items = self.parent.list__categories.findItems(category, Qt.MatchExactly)
			items[0].setIcon(qt.QIcon(''))

	def set_image(self):
		'''
			Insert image to category
		'''
		category = self.category_selected()
		open_file = qt.QFileDialog.getOpenFileName(self.dialog, 'Find Picture', expanduser("~"), 'Picture (*.png *.jpeg *.jpg)')

		if len(open_file) != 0:
			self.dialog.ui.display__image.setPixmap(qt.QPixmap(open_file))
			self.dialog.ui.display__image.show()

			# Delete old category image
			old_name = glob(self.path() + category + '.*')
			if len(old_name) != 0:
				self.parent.data_folder.delete_file(old_name[0])

			# Copy image to <img_cat> directory
			new_name = self.path() + category + os.path.splitext(open_file)[1]
			self.parent.data_folder.copy_to(open_file, new_name)

			# Update GUI
			items = self.parent.list__categories.findItems(category, Qt.MatchExactly)
			items[0].setIcon(qt.QIcon(new_name))
