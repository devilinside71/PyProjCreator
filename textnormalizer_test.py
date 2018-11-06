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

    def test_sample_function(self):
        """Test01
        """

        test_class = textnormalizer.TextNormalizer()
        test_class.string_to_normalize = self.test_str_01
        self.assertEqual(test_class.get_normalized_name(), self.test_res_01)


if __name__ == '__main__':
    unittest.main()
