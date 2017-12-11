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

    