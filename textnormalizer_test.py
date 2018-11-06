# -*- coding: utf-8 -*-
"""
This module tests for __PROJECTNAMELCASE__ module.
"""
import unittest
import textnormalizer


class testFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_str_01 = 'Árvíztűrő tükörfúrógép'
        self.test_res_01 = 'Arvizturo_tukorfurogep'
        self.test_str_02 = 'Árvíztűrő tükörfúrógép'
        self.test_res_02 = 'Arvizturo tukorfurogep'

    def test_get_normalized_name(self):
        """Test for get_normalized_name function.
        """

        test_class = textnormalizer.TextNormalizer()
        test_class.string_to_normalize = self.test_str_01
        self.assertEqual(test_class.get_normalized_name(), self.test_res_01)
        test_class.string_to_normalize = self.test_str_02
        self.assertEqual(test_class.get_normalized_name(), self.test_res_02)


if __name__ == '__main__':
    unittest.main()
