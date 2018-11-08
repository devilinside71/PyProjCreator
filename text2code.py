# -*- coding: utf-8 -*-
"""
This module creates text file with python code from input text file.
"""

import argparse
import logging
import sys


__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'laszlo.devil@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('text2code')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('text2code.log')

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


class Text2Code():
    """Main class.

    """

    def __init__(self):
        self.par_input = ''
        self.par_output = ''
        self.par_variable = ''

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input',
                            help='input file')
        parser.add_argument('-o', '--output',
                            help='output file')
        parser.add_argument('-v', '--variable',
                            help='variable name')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        self.par_input = args.input
        self.par_output = args.output
        self.par_variable = args.variable
        LOGGER.debug('Variable name: %s', self.par_variable)
        LOGGER.debug('Input: %s', self.par_input)
        LOGGER.debug('Output: %s', self.par_output)
        content = ''
        with open(self.par_input, 'r', encoding='utf-8') as myfile:
            content = myfile.readlines()
            content = [x.strip() for x in content]
        out_str = self.par_variable + ' = \'\'' + '\n'
        for line in content:
            line = line.replace('\'', '\\\'')
            out_str += self.par_variable + ' += \'' + line + '\\n\'' + '\n'
        text_file = open(self.par_output, 'w', encoding='utf-8')
        text_file.write(out_str)
        text_file.close()


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = Text2Code()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
