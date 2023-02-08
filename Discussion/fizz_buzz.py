"""
Implement the fizzbuzz sequence, which prints out a single statement for each number from 1 to n. For a number i,

If i is divisible by 3 only, then we print "fizz".
If i is divisible by 5 only, then we print "buzz".
If i is divisible by both 3 and 5, then we print "fizzbuzz".
Otherwise, we print the number i by itself.
"""
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range (1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print ("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print ("buzz")
        else:
            print (i)