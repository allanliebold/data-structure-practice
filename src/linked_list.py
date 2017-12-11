"""Linked list implementation in Python."""


class Node(object):
    """Definition of Node class object."""

    def __init__(self, data, next=None):
        """Initialization of Node."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Definition of Linked List."""

    def __init__(self):
        """Initialization of Linked List."""
        self.head = None
        self._size = 0

    def push(self, data):
        """Add a node containing data to the head of the list."""
        self.head = Node(data, self.head)
        self._size += 1
        return

    def pop(self):
        pass

    def size(self):
        pass

    def remove(self):
        pass

    def display(self):
        pass
