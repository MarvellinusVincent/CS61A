def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    count = 2
    while count != n:
        if n % count == 0:
            n = n // count
            return False
        count += 1
    return True