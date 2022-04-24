import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """
    Fungsi test untuk stack
    """
    def test_1(self):
        """
        should return None when reading an empty Stack
        """
        self.stack = Stack()
        self.assertEqual(self.stack.read(), None)
    
    def test_2(self):
        """
        should return 1 when reading stack with data [1]
        """
        self.stack = Stack()
        self.stack.push(1)
        self.assertEqual(self.stack.read(), 1)
    
    def test_3(self):
        """
        should return 1 when popping a stack with data [1]
        """
        self.stack = Stack()
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

if __name__ == '__main__':
    unittest.main()