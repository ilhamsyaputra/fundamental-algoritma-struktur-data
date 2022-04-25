import unittest
from sort import sort

class TestBubbleSort(unittest.TestCase):
    """
    Fungsi test untuk bubble sort
    """

    def test_1(self):
        """
        should return [] when sorting []
        """
        self.assertEqual(sort([]), [])
    
    def test_2(self):
        """
        should return [1] when sorting [1]
        """
        self.assertEqual(sort([1]), [1])

    def test_3(self):
        """
        should return [1, 2] when sorting [2, 1]
        """
        self.assertEqual(sort([2, 1]), [1, 2])

    def test_4(self):
        """
        should return [1, 2, 4] when sorting [4, 1, 2]
        """
        self.assertEqual(sort([4, 1, 2]), [1, 2, 4])

    def test_5(self):
        """
        should return any unorderd array
        """
        input_array = [4, 2, 1, 5, 6, 3, 9, 8, 0, 7]
        self.assertEqual(sort(input_array), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()