import unittest
from hash import two_sum

class TestHashMap(unittest.TestCase):
    """
    Class untuk test fungsi HashMap
    """

    def test_1(self):
        """
        should return [0, 1] when given ([2, 7, 11, 15], 9)
        """
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums, target), [0, 1])
    
    def test_2(self):
        """
        should return [1, 2] when given ([3, 2, 4], 6)
        """
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(two_sum(nums, target), [1, 2])
    
    def test_3(self):
        """
        should return [0, 1] when given ([3, 3], 6)
        """
        nums = [3, 3]
        target = 6
        self.assertEqual(two_sum(nums, target), [0, 1])


if __name__ == '__main__':
    unittest.main()
    