# -*- coding: utf-8 -*-
"""
This module creates python basic project files in a folder.
"""
# TODO Copyright info, functions, substring, length, unittest

import logging
import sys
import argparse
import os
import errno
# from tkinter import *

logger = logging.getLogger('pyprojcreator')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
logger_fh = logging.FileHandler('pyprojcreator.log')

# create console handler with a higher log level
logger_ch = logging.StreamHandler()
logger_ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
logger_fh.setFormatter(formatter)
logger_ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(logger_fh)
logger.addHandler(logger_ch)


def parse_arguments():
    """
    Parse program arguments.

    @return arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',
                        help='target folder of the project')
    parser.add_argument('-n', '--name',
                        help='name of the project')
    parser.add_argument('-d', '--description',
                        help='description of the project')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()


def execute_program():
    """Execute the program by arguments.
    """

    args = parse_arguments()
    res_name = ""
    res_desc = ""
    res_folder = create_folder(args.folder)
    if res_folder == True:
        res_name = get_projname(args.name)
        res_desc = get_projdesc(args.description)
        if res_name == False or res_desc == False:
            logger.debug("Start GUI to add project name and/or description")
            # https://www.python-course.eu/tkinter_entry_widgets.php
        else:
            logger.debug(
                "No GUI needed to add project name and/or description")
            logger.debug("Project name: '" + args.name)
            logger.debug("Project description: '" + args.description)


def create_folder(folder_name):
    """Create folder for new project.

    Arguments:
        folder_name {str} -- target folder name

    Returns:
        bool -- folder created succesfuly
    """
    ret = False
    logger.debug("Target folder: " + folder_name)
    # Check if folder exists
    folder_exists = os.path.isdir(folder_name)
    if folder_exists:
        logger.debug("Folder '" + folder_name + "' already exists")
    else:
       # create folder
        try:
            os.makedirs(folder_name)
            logger.debug("Folder '" + folder_name + "' created succesfuly")
            ret = True
        except OSError as e:
            ret = False
            if e.errno != errno.EEXIST:
                logger.debug('Cannot create folder ' + folder_name)
                logger.debug('Exit program')
                raise
    return ret


def get_projname(proj_name):
    """Get project name

    Returns:
        str -- project name
    """
    ret = True
    if proj_name == None:
        ret = False
    logger.debug("New project name: '" + str(proj_name) + "'")
    return ret


def get_projdesc(proj_desc):
    """Get project description

    Returns:
        str -- project description
    """
    ret = True
    if proj_desc == None:
        ret = False
    logger.debug("New project description: '" + str(proj_desc) + "'")
    return ret


if __name__ == '__main__':
    logger.debug('Start program')
    execute_program()
    logger.debug('Exit program')
    sys.exit()
