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
    for i in range(10):
        ll.push(i)
    assert ll._size == 10


def test_pop_removes_head():
    """Pop on list with one node empties it."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    assert ll.pop() == 1
    assert not ll.head
    assert ll._size == 0


def test_valid_search_return():
    """Search with valid data should return the correct node."""
    from linked_list import LinkedList
    ll = LinkedList()
    for i in range(10):
        ll.push(i)
    assert ll.search(5).data == 5


def test_valid_search_head_node():
    """Search with valid data returns correct node if it is the head."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(3)
    assert ll.search(3) == ll.head


def test_invalid_search():
    """Search with data not in the list returns None."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(2)
    ll.push(4)
    ll.push(6)
    assert ll.search(8) is None


def test_remove_valid_node():
    """Successfully remove the node with the specified data."""
    from linked_list import LinkedList
    ll = LinkedList()
    for i in range(5):
        ll.push(i)
    assert ll.remove(2) == 2
    assert len(ll) == 4
    assert ll.head.next.data == 3


def test_remove_head():
    """Remove with data in head node pops it from the list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    assert ll.remove(3) == 3
    assert ll.head.data == 2
    assert len(ll) == 2


def test_remove_head_only_node():
    """Remove the head in a list with only one node."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    assert ll.remove(1) == 1
    assert not ll.head
    assert len(ll) == 0


def test_display():
    """Display method returns string of data in the list in order."""
    from linked_list import LinkedList
    ll = LinkedList()
    for i in range(1, 11):
        ll.push(i)
    assert ll.display() == '(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)'
