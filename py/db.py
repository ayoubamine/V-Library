# -*- coding: utf-8 -*-

import sqlite3


class DB():
	def __init__(self, HOME_DIR):
		self.HOME_DIR = HOME_DIR
		# Opens a connection to the SQLite database file database
		self.conn = sqlite3.connect(self.HOME_DIR + 'V-Library.db')
		# A Cursor instance has the following attributes and methods
		self.cursor = self.conn.cursor()
		# Executes an SQL statement
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Category(name TEXT, sort INTEGER)')

	def __len__(self):
		self.cursor.execute('SELECT count() FROM Category')
		return self.cursor.fetchone()[0]

	def close(self):
		'''
			Close the cursor and database connection
		'''
		self.cursor.close()
		self.conn.close()

	def add_category(self, name, sort):
		'''
			Add new category name
		'''
		self.cursor.execute('INSERT INTO Category (name, sort) VALUES(?, ?)', (name, sort))
		self.conn.commit()

	def search_by_name(self, name):
		'''
			Check a category name exists in database
		'''
		self.cursor.execute('SELECT name FROM Category WHERE name = ?', (name,))
		data = self.cursor.fetchall()

		if len(data) > 0:
			return False
		return True

	def all_categories(self):
		'''
			Get all categories from database
		'''
		self.cursor.execute('SELECT name FROM Category ORDER BY sort DESC')
		data = self.cursor.fetchall()

		return data

	def delete_category(self, category_selected):
		'''
			Delete category row from database
		'''
		self.cursor.execute("DELETE FROM Category WHERE name = ?", (category_selected,))
		self.conn.commit()

	def update_category(self, old_text, new_text):
		'''
			Update category name
		'''
		self.cursor.execute("UPDATE Category SET name=? WHERE name=?", (new_text, old_text))
		self.conn.commit()

	def reorder_categories(self, sort, name):
		'''
			Reorder all categories
		'''
		self.cursor.execute("UPDATE Category SET sort=? WHERE name=?", (sort, name))
		self.conn.commit()
