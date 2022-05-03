from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, node = None):
        node = node or self.root
 
        if node is None:
            self.root = Node(value)
            node = self.root
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)

    def leftmost_node(self, node):
        if node.left is None:
            return node
        return self.leftmost_node(node.left)

    def delete(self, value, node = None, parent_node = None, mark = None):
        node = node or self.root

        if node is None:
            return None
        
        if value == node.value:
            deleted_node = node

            if node == self.root:
                if node.left is None and node.right is None:
                    self.root = None
                else:
                    self.root = self.leftmost_node(node.right)
            else:
                if mark == 'left':
                    if node.left is not None and node.right is None:
                        parent_node.left = node.left
                    else:
                        parent_node.left = node.right
                elif mark == 'right':
                    if node.right is not None and node.left is None:
                        parent_node.right = node.right
                    else:
                        parent_node.right = node.left

        elif value < node.value:
            deleted_node = self.delete(value, node.left, node, 'left')
        elif value > node.value:
            deleted_node = self.delete(value, node.right, node, 'right')
            
        return deleted_node
