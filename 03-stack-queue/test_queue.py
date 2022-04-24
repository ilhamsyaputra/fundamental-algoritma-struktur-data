import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    """
    fungsi test untuk queue
    """

    def test_1(self):
        """
        should return None when reading an empty queue
        """
        self.queue = Queue()
        self.assertEqual(self.queue.read(), None)

    def test_2(self):
        """
        should return 1 when reading queue with data [1]
        """
        self.queue = Queue()
        self.queue.push(1)
        self.assertEqual(self.queue.read(), 1)

    def test_3(self):
        """
        should return 1 when popping a queue with data [1, 2]
        """
        self.queue = Queue()
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)