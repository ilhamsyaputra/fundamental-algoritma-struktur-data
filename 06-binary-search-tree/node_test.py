import unittest
from node import Node

class TestNode(unittest.TestCase):
    """
    Class untuk test node
    """

    def test_1(self):
        """
        should return value 1 if we initiate with 1
        """
        node = Node(1)
        self.assertEqual(node.value, 1)

    def test_2(self):
        """
        node.left should return None when first initialized
        """
        node = Node(1)
        self.assertEqual(node.left, None)

    def test_3(self):
        """
        node.right should return None when first initialized
        """
        node = Node(1)
        self.assertEqual(node.right, None)