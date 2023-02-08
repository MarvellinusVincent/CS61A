"""
Write a function that takes in a linked list and returns the sum of all its elements.
You may assume all elements in s are integers. Try to implement this recursively!
"""

def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    # Recursive solution:
    if s.rest == Link.empty:
        return s.first
    return s.first + sum_nums(s.rest)

    # Iterative solution:
    # sum = 0
    # while s != Link.empty:
    #     sum += s.first
    #     s = (s.rest)
    return sum

class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'