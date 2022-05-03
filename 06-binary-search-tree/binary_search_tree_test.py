import unittest
from binary_search_tree import BinarySearchTree

class TestBST(unittest.TestCase):
    """
    class untuk test binary search tree
    """

    def test_1(self):
        """
        BST.root should return None when first initialized
        """
        BST = BinarySearchTree()
        self.assertEqual(BST.root, None)

    def test_2(self):
        """
        BST.root.value should return 1 when we insert 1
        """
        BST = BinarySearchTree()
        BST.insert(1)
        self.assertEqual(BST.root.value, 1)
    
    def test_3(self):
        """
        should add value to left node when adding value lower than root/parent
        """
        BST = BinarySearchTree()
        BST.insert(2)
        BST.insert(1)
        self.assertEqual(BST.root.left.value, 1)

    def test_4(self):
        """
        should add value to right node when adding value higher than root/parent
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(2)
        self.assertEqual(BST.root.right.value, 2)
    
    def test_5(self):
        """
        should add value to left grandchild node when adding value smaller than ancestor left node
        """
        BST = BinarySearchTree()
        BST.insert(3)
        BST.insert(2)
        BST.insert(1)
        self.assertEqual(BST.root.left.left.value, 1)

    def test_6(self):
        """
        should add value to right grandchild node when adding value bigger than ancestor right node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(2)
        BST.insert(3)
        self.assertEqual(BST.root.right.right.value, 3)
    
    def test_7(self):
        """
        
        """
        BST = BinarySearchTree()
        BST.insert(4)
        BST.insert(2)
        BST.insert(6)
        BST.insert(1)
        BST.insert(3)
        BST.insert(5)
        BST.insert(7)
        self.assertEqual(BST.root.right.left.value, 5)
        