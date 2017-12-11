"""Linked List tests."""


def test_node_has_attributes():
    """Node object has data and next attributes."""
    from linked_list import Node
    n = Node(1)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')
