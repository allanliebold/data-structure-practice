"""Tree made up of lists."""


def binary_tree(r):
    """Definition of a binary tree using lists."""
    return [r, [], []]


def insert_left(root, new_branch):
    """Insert a branch to the left."""
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def get_root_val(root):
    """Return the value of the root."""
    return root[0]


def set_root_val(root, new_val):
    """Set a new value for the root."""
    root[0] = new_val
