# -*- coding: utf-8 -*-
"""
This module normalizes strings.
"""
import sys


class TextNormalizer():
    """Main class.
    """

    def __init__(self):
        self.string_to_normalize = ''

    def execute_program(self):
        """Execute the program.
        """
        pass

    def get_normalized_name(self):
        """Replace non US characters

        Arguments:
            name_str {str} -- string to normalize

        Returns:
            str -- normalized string
        """

        res = self.string_to_normalize
        res = res.replace('á', 'a')
        res = res.replace('Á', 'A')
        res = res.replace('é', 'e')
        res = res.replace('É', 'E')
        res = res.replace('ö', 'o')
        res = res.replace('Ö', 'O')
        res = res.replace('ő', 'o')
        res = res.replace('Ő', 'O')
        res = res.replace('ó', 'o')
        res = res.replace('Ó', 'O')
        res = res.replace('ü', 'u')
        res = res.replace('Ü', 'U')
        res = res.replace('ű', 'u')
        res = res.replace('Ű', 'U')
        res = res.replace('ú', 'u')
        res = res.replace('Ú', 'U')
        res = res.replace('í', 'i')
        res = res.replace('Í', 'i')
        res = res.replace(' ', '_')
        res = res.replace('.', '_')
        res = res.replace(':', '_')
        return res


if __name__ == '__main__':
    PROG = TextNormalizer()
    PROG.string_to_normalize = 'Árvíztűrő tükörfúrógép'
    print(PROG.get_normalized_name())
    sys.exit()
