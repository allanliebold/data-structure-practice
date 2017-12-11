"""Linked List tests."""


def test_node_has_attributes():
    """Node object has data and next attributes."""
    from linked_list import Node
    n = Node(1)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')


def test_list_has_attributes():
    """Linked List has expected attributes on initialization."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert hasattr(ll, 'head')
    assert hasattr(ll, '_size')
    assert not ll.head
    assert ll._size == 0


def test_pushed_node_is_head():
    """Pushing a new node to empty list makes it the head."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    assert ll.head.data == 1


def test_pushing_nodes_adds_to_size():
    """Push should increase the size attribute of the list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    assert ll._size == 3
