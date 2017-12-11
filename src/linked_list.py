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
        new_head = Node(data, self.head)
        self.head = new_head
        self._size += 1
        return

    def pop(self):
        """Remove the node at the head of the list."""
        popped = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.next = None
        self._size -= 1
        return popped

    def size(self):
        """Return the number of nodes in the list."""
        return self._size

    def __len__(self):
        """Return size with built in len function."""
        return self._size

    def search(self, data):
        """Return the node containing the passed data, if it exists."""
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return

    def remove(self, data):
        """Remove the node with specified data from the list, if it exists."""
        target = self.search(data)
        if not target:
            return

        if target == self.head:
            return self.pop()

        curr = self.head

        while curr.next != target:
            curr = curr.next

        curr.next = target.next
        self._size -= 1
        return target.data

    def display(self):
        """Return a string containing data in the list."""
        contents = '('
        curr = self.head
        while curr.next:
            contents += str(curr.data) + ', '
            curr = curr.next
        contents += str(curr.data) + ')'
        return contents
