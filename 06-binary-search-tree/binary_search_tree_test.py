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

    def test_deletion_1(self):
        """
        should return None when deleting any value from an empty tree
        """
        BST = BinarySearchTree()
        self.assertEqual(BST.delete(1), None)

    def test_deletion_2(self):
        """
        should return root node when deleting root node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        deleted_node = BST.delete(1)
        self.assertEqual(deleted_node.value, 1)
        
    def test_deletion_3(self):
        """
        should actually delete the root node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.delete(1)
        self.assertEqual(BST.root, None)

    def test_deletion_4(self):
        """
        should return left child node when deleting child node
        """
        BST = BinarySearchTree()
        BST.insert(2)
        BST.insert(1)
        deleted_node = BST.delete(1)
        self.assertEqual(deleted_node.value, 1)

    def test_deletion_5(self):
        """
        should actually delete left child node
        """
        BST = BinarySearchTree()
        BST.insert(2)
        BST.insert(1)
        BST.delete(1)
        self.assertEqual(BST.root.left, None)

    def test_deletion_6(self):
        """
        should return right child node when deleting child node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(2)
        deleted_node = BST.delete(2)
        self.assertEqual(deleted_node.value, 2)

    def test_deletion_7(self):
        """
        should actually delete right child node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(2)
        BST.delete(2)
        self.assertEqual(BST.root.right, None)

    def test_deletion_8(self):
        """
        should ensure left grandchild node become the new child node
        """
        BST = BinarySearchTree()
        BST.insert(3)
        BST.insert(2)
        BST.insert(1)
        BST.delete(2)
        self.assertEqual(BST.root.left.value, 1)

    def test_deletion_9(self):
        """
        should ensure right grandchild node become the new child node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(2)
        BST.insert(3)
        BST.delete(2)
        self.assertEqual(BST.root.right.value, 3)

    def test_deletion_10(self):
        """
        should ensure right grandchild node become new left child node
        """
        BST = BinarySearchTree()
        BST.insert(3)
        BST.insert(1)
        BST.insert(2)
        BST.delete(1)
        self.assertEqual(BST.root.left.value, 2)

    def test_deletion_11(self):
        """
        should ensure left grandchild node become new right child node
        """
        BST = BinarySearchTree()
        BST.insert(1)
        BST.insert(3)
        BST.insert(2)
        BST.delete(3)
        self.assertEqual(BST.root.right.value, 2)

    def test_deletion_12(self):
        """
        should ensure left-most node of the right subtree become the new left child node
        """
        BST = BinarySearchTree()
        BST.insert(4)
        BST.insert(2)
        BST.insert(5)
        BST.insert(1)
        BST.insert(3)
        BST.delete(2)
        self.assertEqual(BST.root.left.value, 3)
    
    def test_deletion_13(self):
        """
        should ensure left most node of the right subtree become the new root node
        """
        BST = BinarySearchTree()
        BST.insert(2)
        BST.insert(1)
        BST.insert(4)
        BST.insert(3)
        BST.insert(5)
        BST.delete(2)
        self.assertEqual(BST.root.value, 3)

    def test_deletion_14(self):
        """
        should ensure left most node of the right subtree become the new parent node
        """
        BST = BinarySearchTree()
        BST.insert(8)
        BST.insert(4)
        BST.insert(12)
        BST.insert(2)
        BST.insert(6)
        BST.insert(10)
        BST.insert(14)
        BST.insert(1)
        BST.insert(3)
        BST.insert(5)
        BST.insert(7)
        BST.insert(9)
        BST.insert(11)
        BST.insert(13)
        BST.insert(15)
        BST.delete(8)
        self.assertEqual(BST.root.value, 9)