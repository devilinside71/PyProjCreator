# -*- coding: utf-8 -*-
"""
This module creates python basic project files in a folder.
"""
# TODO Copyright info, functions, substring, length, unittest

import logging
import sys
import argparse

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
    parser.add_argument('-cc', '--catalogcode', help='catalog barcode')
    parser.add_argument('-cn', '--catalognumber', help='catalog number')
    parser.add_argument('-lc', '--lotcode', help='LOT barcode')
    parser.add_argument('-ln', '--lotnumber', help='LOT number')
    parser.add_argument('-li', '--lic', help='LIC identifier')
    parser.add_argument('-um', '--unitofmeasure', help='Unit of Measure')
    parser.add_argument('-f', '--function', help='function to execute',
                        type=str, choices=['get_lic', 'check_lic_length',
                                           'check_lic_first_char',
                                           'check_code_start',
                                           'get_catalog_number',
                                           'get_unit_of_measure',
                                           'get_sum_of_digits',
                                           'calculate_checkdigit',
                                           'get_checkdigit',
                                           'create_catalog_code',
                                           'check_lot_code_start',
                                           'get_lot_number',
                                           'get_link_char_from_catalog_code',
                                           'get_link_char'
                                           ])
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()


def execute_program():
    """Execute the program by arguments.
    """

    args = parse_arguments()
    if args.function == 'get_lic':
        res = str(get_lic(args.catalogcode))
        if args.verbose:
            print("LIC: " + res)
        else:
            print(res)


def get_lic(code):
    """Get LIC Labeler Identification Code.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        str -- LIC code
    """

    ret = code[1:5]
    return ret


if __name__ == '__main__':
    logger.debug('Start program')
    execute_program()
    logger.debug('Exit program')
    sys.exit()
