def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
    total = 0
    for num in range (start, stop):
        total = total + num
    return total
"""
Recursive way:
    if start == stop:
        return start
    else:
        return start + add_in_range(start + 1, stop)
"""