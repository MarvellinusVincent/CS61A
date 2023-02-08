def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    def helper(num, prev_digit=-1, lastHasNeighbor = False):
        if num==0:
            return 0
        elif num%10==prev_digit:
            if lastHasNeighbor:
                return 1 + helper(num//10, prev_digit = num%10, lastHasNeighbor = True)
            else:
                return 2 + helper(num//10, prev_digit = num%10, lastHasNeighbor = True)
        else:
            return helper(num//10, prev_digit = num%10, lastHasNeighbor = False)
    return helper(num, prev_digit=-1, lastHasNeighbor = False)