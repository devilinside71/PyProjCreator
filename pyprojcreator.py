# -*- coding: utf-8 -*-
"""
This module creates python basic project files in a folder.
"""

import argparse
import errno
import logging
import os
import sys
from tkinter import Label, Entry, Button, W, END, Tk, filedialog
from textnormalizer import TextNormalizer

__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'laszlo.devil@gmail.com'
__status__ = 'Initial'


LOGGER = logging.getLogger('pyprojcreator')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('pyprojcreator.log')

# create console handler with a higher log level
LOGGER_CH = logging.StreamHandler()
LOGGER_CH.setLevel(logging.INFO)

# create FORMATTER and add it to the handlers
FORMATTER = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
LOGGER_FH.setFormatter(FORMATTER)
LOGGER_CH.setFormatter(FORMATTER)

# add the handlers to the LOGGER
LOGGER.addHandler(LOGGER_FH)
LOGGER.addHandler(LOGGER_CH)


class ProjCreatorProgram():
    """Main class.

    """

    def __init__(self):
        self.master = Tk()
        self.entry_folder = Entry(self.master)
        self.entry_name = Entry(self.master)
        self.entry_desc = Entry(self.master)
        self.entry_author = Entry(self.master)
        self.project_name = ''
        self.project_desc = ''
        self.folder_name = ''
        self.project_author = ''
        self.folder_created_by_dialog = False

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--folder',
                            help='target folder of the project')
        parser.add_argument('-n', '--name',
                            help='name of the project')
        parser.add_argument('-d', '--description',
                            help='description of the project')
        parser.add_argument('-a', '--author',
                            help='author of the project')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        self.folder_name = args.folder
        self.project_name = args.name
        self.project_desc = args.description
        self.project_author = args.author
        self.folder_created_by_dialog = False
        if self.folder_name is None:
            self.folder_name = ''
        if self.project_name is None:
            self.project_name = ''
        if self.project_desc is None:
            self.project_desc = 'This class module is...'
        if self.project_author is None:
            self.project_author = 'Laszlo Tamas'
        if self.folder_name == '' or self.project_name == '' or self.project_desc == '' or self.project_author == '':
            Label(self.master, text='Folder Name').grid(row=0)
            self.entry_folder.delete(0, END)
            self.entry_folder.insert(0, self.folder_name)
            self.entry_folder.grid(row=0, column=1)
            Label(self.master, text='Project Name').grid(row=1)
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, self.project_name)
            self.entry_name.grid(row=1, column=1)
            Label(self.master, text='Project Desc').grid(row=2)
            self.entry_desc.delete(0, END)
            self.entry_desc.insert(0, self.project_desc)
            self.entry_desc.grid(row=2, column=1)
            # self.entry_desc.config(width=30)
            Label(self.master, text='Author').grid(row=3)
            self.entry_author.delete(0, END)
            self.entry_author.insert(0, self.project_author)
            self.entry_author.grid(row=3, column=1)
            Button(self.master, text='OK', command=self.set_project).grid(row=4, column=0, sticky=W, pady=4)
            Button(self.master, text='Cancel', command=self.master.quit).grid(row=4, column=1, sticky=W, pady=4)
            Button(self.master, text='Browse', command=self.set_folder).grid(row=0, column=2, sticky=W, pady=4)

            self.master.title('Project creator')
            # self.master.geometry('500x130')
            self.master.mainloop()
        else:
            LOGGER.debug('Project name: %s', self.project_name)
            LOGGER.debug('Project description: %s', self.project_desc)
            self.create_project()

    @staticmethod
    def create_folder(folder_name):
        """Create folder for new project.

        Arguments:
            folder_name {str} -- target folder name

        Returns:
            bool -- folder created succesfuly
        """
        ret = False
        LOGGER.debug('Target folder: %s', folder_name)
        # Check if folder exists
        folder_exists = os.path.isdir(folder_name)
        if folder_exists:
            LOGGER.debug('Folder "%s" already exists', folder_name)
        else:
            # create folder
            try:
                os.makedirs(folder_name)
                LOGGER.debug('Folder "%s" created succesfuly', folder_name)
                ret = True
            except OSError as os_err:
                ret = False
                if os_err.errno != errno.EEXIST:
                    LOGGER.debug('Cannot create folder %s', folder_name)
                    LOGGER.debug('Exit program')
                    raise
        return ret

    def set_project(self):
        """Setup variables from GUI for project creation.
        """

        self.folder_name = self.entry_folder.get()
        self.project_name = self.entry_name.get()
        self.project_desc = self.entry_desc.get()
        self.project_author = self.entry_author.get()
        LOGGER.debug('Project name: %s', self.project_name)
        LOGGER.debug('Project description: %s', self.project_desc)
        LOGGER.debug('Author: %s', self.project_author)
        self.master.quit()
        self.create_project()

    def set_folder(self):
        """Set the project folder by filedialog.
        """

        self.folder_name = filedialog.askdirectory()
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, self.folder_name)
        LOGGER.debug('Folder name: %s', self.folder_name)
        self.folder_created_by_dialog = True

    def create_project(self):
        """Create project.
        """

        if self.create_folder(self.folder_name) or self.folder_created_by_dialog:
            text_norm = TextNormalizer()
            # Create main file
            with open('sample01.py', 'r') as myfile:
                data = myfile.read()
                data = data.replace('__AUTHOR__', self.project_author)
                text_norm.string_to_normalize = self.project_name
                data = data.replace('__PROJECTNAME__',
                                    text_norm.normalized_name())
                data = data.replace('__PROJECTNAMELCASE__',
                                    text_norm.normalized_name().lower())
                data = data.replace('__DESCRIPTION__', self.project_desc)
                # print(data)
                text_file = open(self.folder_name + '\\' + text_norm.normalized_name().lower() + '.py', 'w',
                                 encoding='utf-8')
                text_file.write(data)
                text_file.close()
            # Create unittest file
            with open('sample01_test.py', 'r') as myfile:
                data = myfile.read()
                data = data.replace('__PROJECTNAME__',
                                    text_norm.normalized_name())
                data = data.replace('__PROJECTNAMELCASE__',
                                    text_norm.normalized_name().lower())
                data = data.replace('__DESCRIPTION__', self.project_desc)
                # print(data)
                text_file = open(self.folder_name + '\\' + text_norm.normalized_name().lower() + '_test.py', 'w',
                                 encoding='utf-8')
                text_file.write(data)
                text_file.close()
            # Create notes text file
            with open('sample01_notes.txt', 'r') as myfile:
                data = myfile.read()
                data = data.replace('__PROJECTNAME__',
                                    text_norm.normalized_name())
                data = data.replace('__PROJECTNAMELCASE__',
                                    text_norm.normalized_name().lower())
                data = data.replace('__DESCRIPTION__', self.project_desc)
                # print(data)
                text_file = open(self.folder_name + '\\' + text_norm.normalized_name().lower() + '_notes.txt', 'w',
                                 encoding='utf-8')
                text_file.write(data)
                text_file.close()
        else:
            sys.exit()


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = ProjCreatorProgram()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
