"""
Q7: Leaves
Write a function leaves that returns a list of all the label values of the leaf nodes of a Tree.
"""

def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return [t.label]
    all_leaves = []
    for branch in t.branches:
        all_leaves += leaves(branch)
    return all_leaves

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches