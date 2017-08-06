# -*- coding: utf-8 -*-

from PyQt4.QtCore import (QThread, pyqtSignal, SIGNAL)
from py.data_folder import DataFolder
from zipfile import ZipFile, ZIP_DEFLATED
from PyPDF2 import PdfFileReader
from wand.image import Image
from glob import glob
from json import dump
import os


class BackupThread(QThread):
    '''
        Zip thread
    '''
    def __init__(self, backup_file, path, categories):
        QThread.__init__(self)
        self.backup_file = backup_file
        self.path = path
        self.categories = categories

    def run(self):

        with ZipFile(self.backup_file, 'w', ZIP_DEFLATED) as zip:

            zip.comment = b'V-Library'

            for root, dirs, files in os.walk(self.path):
                
                split_root = root[len(self.path) + 1:]
                split_root = split_root.split(os.sep, maxsplit = 1)[0]
                
                if split_root in self.categories:
                    for file in files:
                        file = os.path.join(root, file)
                        split_file = file[len(self.path) + 1:]
                        # Zip file
                        zip.write(file, split_file)


class RestoreThread(QThread):
    '''
        Extract zip thread
    '''
    def __init__(self, HOME_DIR, restore_file, restore_dir):
        QThread.__init__(self)
        self.data_folder = DataFolder(HOME_DIR)
        self.HOME_DIR = HOME_DIR
        self.restore_file = restore_file
        self.restore_dir = restore_dir

    def isvalid(self, path):
        '''
            Check backup file is valid
        '''
        for category in os.listdir(path):
            if os.path.exists(path + category + '/data') and os.path.exists(path + category + '/images') and os.path.exists(path + category + '/books'):
                for file in os.listdir(path + category + '/data'):
                    if not file.endswith('.txt'): return False
                for file in os.listdir(path + category + '/images'):
                    if not file.endswith('.png'): return False
                for file in os.listdir(path + category + '/books'):
                    if not file.endswith('.pdf'): return False
                for file in os.listdir(path + category):
                    if os.path.isfile(file):
                        if not (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg')): return False
            else:
                return False

        return True

    def run(self):

        try:
            # Upzip file
            with ZipFile(self.restore_file, 'r') as unzip:
                unzip.extractall(self.restore_dir)

            if self.isvalid(self.restore_dir):
                # Get list direction from restore path
                categories = os.listdir(self.restore_dir)

                # Save in data folder
                for category in categories:
                    generate = self.data_folder.generate_category_name(category)
                    
                    if generate != category:
                        categories[categories.index(category)] = generate
                        image_category = glob(self.restore_dir + category + '/' + category + '.*')
                        if len(image_category) != 0:
                            name, ext = os.path.splitext(image_category[0])
                            self.data_folder.rename(self.restore_dir + category, category + ext, generate + ext)
                    
                    self.data_folder.copy_folder_to(self.restore_dir + category, self.HOME_DIR + 'Data/' + generate)

                # Delete restore folder
                self.data_folder.delete_folder(self.restore_dir)
                
                self.emit(SIGNAL('RESTORE'), True, categories)
            else:
                raise Exception('file not valid !!')
        except:
            if os.path.exists(self.restore_dir): self.data_folder.delete_folder(self.restore_dir)
            self.emit(SIGNAL('RESTORE'), False)


class AddBooksThread(QThread):
    '''
        Create thread
    '''
    def __init__(self, files, directory, HOME_DIR):
        QThread.__init__(self)
        self.files = files
        self.directory = directory
        self.HOME_DIR = HOME_DIR
        self.data_folder = DataFolder()

    update = pyqtSignal()
    done = pyqtSignal(object)

    def run(self):

        for file in self.files:
            generate = self.data_folder.generate_book_name(self.directory + 'books/' + os.path.basename(file))
            # Copy file to the category selected
            self.data_folder.copy_to(file, self.directory + 'books/' + generate)
            # Replace file path with file name
            self.files[self.files.index(file)] = os.path.splitext(generate)[0]
            
            file_name = self.directory + 'books/' + generate
            image_name = self.directory + 'images/' + os.path.splitext(generate)[0] + '.png'
            txt_name = self.directory + 'data/' + os.path.splitext(generate)[0] + '.txt'
            data = {}

            try:
                # Convert first page of file pdf to image (.png)
                # Documentation: http://docs.wand-py.org/en/0.4.4/
                with Image(filename = file_name + '[0]') as image:
                    image.save(filename = image_name)
            
            except UnicodeEncodeError:
                try:
                    # Solve problem of Unicode Encode Error
                    with Image(filename = file + '[0]') as image:
                        img = self.HOME_DIR + os.path.basename(image_name)
                        image.save(filename = img)

                    self.data_folder.move_to(img, image_name)

                except:
                    pass
            except:
                pass
            
            try:
                '''
                    Initializes a PdfFileReader object
                    Parameters: 
                        stream – String representing a path to a PDF file.
                        strict (bool) – Determines whether user should be warned of all problems and also causes some correctable problems to be fatal.
                
                    Documentation: https://pythonhosted.org/PyPDF2/
                '''
                pdf_info = PdfFileReader(file_name, strict = False)
                # An object that represents Adobe XMP metadata
                author = pdf_info.getXmpMetadata().dc_creator
                # Calculates the number of pages in this PDF file
                pages = pdf_info.getNumPages()

                if len(author) > 0: data['authors'] = ', '.join(author)
                data['pages'] = pages
            except:
                pass

            with open(txt_name, 'w') as outfile:
                # Python object to JSON document
                dump(data, outfile)
            
            # Connect to progress_bar() function
            self.update.emit()

        # Connect to backup_result() function
        self.done.emit(self.files)


class ResetImage(QThread):
    '''
        Zip thread
    '''
    def __init__(self, HOME_DIR, path, book_path):
        QThread.__init__(self)
        self.HOME_DIR = HOME_DIR
        self.path = path
        self.book_path = book_path
        self.data_folder = DataFolder()

    def run(self):

        try:
            # Convert first page of file pdf to image (.png)
            # Documentation: http://docs.wand-py.org/en/0.4.4/
            with Image(filename = self.book_path + '[0]') as img:
                img.save(filename = self.path)

            self.emit(SIGNAL('END'), self.path)

        except UnicodeEncodeError:
            try:
                # Solve problem of Unicode Encode Error
                new_book_path = self.HOME_DIR + os.path.basename(self.book_path)
                new_image_path = self.HOME_DIR + os.path.basename(self.path)
                # Copy book to HOME DIRECTORY
                self.data_folder.copy_to(self.book_path, new_book_path)
                
                # Convert first page of file pdf to image (.png)
                with Image(filename = new_book_path + '[0]') as image:
                    image.save(filename = new_image_path)

                # Delete the copy
                self.data_folder.delete_file(new_book_path)
                # Move image book
                self.data_folder.move_to(new_image_path, self.path)

                self.emit(SIGNAL('END'), self.path)
            
            except:
                if os.path.exists(new_book_path): self.data_folder.delete_file(new_book_path)
                self.emit(SIGNAL('END'))

        except:
            self.emit(SIGNAL('END'))
