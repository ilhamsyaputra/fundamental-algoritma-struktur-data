# python -m unittest -v test_linear_search.py

import unittest
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    """
    Test fungsi linear search
    """
    def test_should_return_none_empty_list(self):
        """
        should return None if empty list given in first argument
        """
        self.assertEqual(linear_search([0], 1), None)
    
    def test_should_return_0_when_searching_1_in_2_element_array(self):
        """
        should return 0 when searching 1 in [0, 1] array
        """
        self.assertEqual(linear_search([0, 1], 1), 1)

    def test_should_return_none_when_searching_1_in_no_1_array(self):
        """
        should return None when searching 1 in [0, 2] array
        """
        self.assertEqual(linear_search([0, 2], 1), None)

    def test_should_return_7_in_given_array(self):
        """
        should return 7 in [3, 7, 15, 23, 46, 59, 63, 72, 88, 95] array
        """
        self.assertEqual(linear_search([3, 7, 15, 23, 46, 59, 63, 72, 88, 95], 72), 7)


if __name__ == '__main__':
    unittest.main()
