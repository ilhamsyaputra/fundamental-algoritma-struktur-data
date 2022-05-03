from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.right = None
        self.left = None

    def insert(self, value, node = None):
        node = node or self.root

        if node is None:
            self.root = Node(value)
            node = self.root

        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.left = node.left
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                self.right = node.right
            else:
                self.insert(value, node.right)
