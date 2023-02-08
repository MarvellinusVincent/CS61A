"""
Q4: Multiply Links
Write a function that takes in a Python list of linked lists and multiplies them element-wise. 
It should return a new linked list.

If not all of the Link objects are of equal length, 
return a linked list whose length is that of the shortest linked list given. 
You may assume the Link objects are shallow linked lists, and that lst_of_lnks contains at least one linked list.
"""

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        product *= link.first
        rest_list = [link.rest for link in lst_of_lnks]
    return Link(product, multiply_lnks(rest_list))

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