# -*- coding: utf-8 -*-

from shutil import (copytree, copy, rmtree, move)
import os


class DataFolder():
	def __init__(self, HOME_DIR = None):
		if HOME_DIR is not None:
			self.HOME_DIR = HOME_DIR

	def create_folders(self):
		'''
			Create folders if not exists.
			--> V-Library-Data
					--> Data
		'''
		
		if not os.path.exists(self.HOME_DIR):
			os.makedirs(self.HOME_DIR)
		
		if not os.path.exists(self.HOME_DIR + 'Data'):
			os.makedirs(self.HOME_DIR + 'Data')

	def generate_category_name(self, name):
		'''
			Return category name based on old name
		'''
		while os.path.exists(self.HOME_DIR + 'Data/' + name):
			name_split = name.split('_')
			if len(name_split) > 1 and name_split[-1].isnumeric():
				name_split[-1] = str(int(name_split[-1]) + 1)
				name =  '_'.join(name_split)
			else:
				name += '_1'
		
		return name

	def generate_book_name(self, file):
		'''
			Return book name based on old name
		'''
		directory = os.path.dirname(file) + '/'
		name, ext = os.path.splitext(os.path.basename(file))
		
		while os.path.exists(directory + name + ext):
			name_split = name.split('_')
			if len(name_split) > 1 and name_split[-1].isnumeric():
				name_split[-1] = str(int(name_split[-1]) + 1)
				name =  '_'.join(name_split)
			else:
				name += '_1'
		
		return os.path.basename(directory + name + ext)

	def add_folder(self, path):
		'''
			Recursive directory creation function.
		'''
		os.makedirs(path)

	def delete_folder(self, path):
		'''
			Delete a directory and all its contents.
		'''

		rmtree(path)

	def delete_file(self, path):
		'''
			Delete the file path.
		'''
		os.remove(path)

	def rename(self, path, old_name, new_name):
		'''
			Rename the file or directory: src to dst.
		'''
		os.rename(path + '/' + old_name, path + '/' + new_name)

	def copy_to(self, src, dst):
		'''
			Copies the file src to the file or directory dst.
			src and dst should be strings.
			If dst specifies a directory, the file will be copied into dst using the base filename from src.
		'''
		copy(src, dst)

	def copy_folder_to(self, src, dst):
		'''
			Recursively copy an entire directory tree rooted at src to dst
		'''
		copytree(src, dst)

	def move_to(self, src, dst):
		'''
			Recursively move a file or directory (src) to another location (dst)
		'''
		move(src, dst)
