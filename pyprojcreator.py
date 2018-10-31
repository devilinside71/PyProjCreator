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

logger = logging.getLogger('program')
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
    parser.add_argument('-pf', '--projectfolder',
                        help='target folder of the project')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()


def execute_program():
    """Execute the program by arguments.
    """

    args = parse_arguments()
    create_folder(args.projectfolder, args.verbose)


def create_folder(folder_name, verbosity):
    """Create folder for new project.

    Arguments:
        folder_name {str} -- target folder name

    """
    if verbosity:
        print("Target folder: " + folder_name)
    else:
        print(folder_name)
    # Check if folder exists
    folder_exists = os.path.isdir(folder_name)
    if folder_exists:
        if verbosity:
            print("Folder '" + folder_name + "' already exists")
        else:
            print(str(folder_exists))
    else:
       # create folder
        try:
            os.makedirs(folder_name)
            # code here
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


if __name__ == '__main__':
    logger.debug('Start program')
    execute_program()
    logger.debug('Exit program')
    sys.exit()
