def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n != 0:
        if n % 10 == count and count == k:
            return True
        count += 1
        n = n // 10
    return False
    # k2 = k+1
    # n = n%10**k2//10**k
    # if n==k:
    #     return True
    # return False