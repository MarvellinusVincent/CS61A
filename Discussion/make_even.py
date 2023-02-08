"""
Q6: Make Even
Define a function make_even which takes in a tree t whose values are integers, 
and mutates the tree such that all the odd integers are increased by 1 and all the even integers remain the same.
"""

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2 != 0:
        t.label += 1
    for branch in t.branches:
        return make_even(branch)
    return

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches