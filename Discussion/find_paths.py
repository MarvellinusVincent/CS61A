"""Q8: Find Paths
Hint: This question is similar to find_path on Discussion 05.

Define the procedure find_paths that, given a Tree t and an entry,
returns a list of lists containing the nodes along each path from the root of t to entry. 
You may return the paths in any order.

For instance, for the following tree tree_ex, find_paths should behave as specified in the function doctests
"""

def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if t.label == entry:
        paths.append([t.label])
    for branch in t.branches:
        for path in find_paths(branch, entry):
            paths.append([t.label] + path)
    return paths

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches