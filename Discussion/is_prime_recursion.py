"""
Q6: Is Prime
Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise. 
Assume n > 1. We implemented this in Discussion 1 iteratively, now time to do it recursively!

Hint: You will need a helper function! Remember helper functions are nested functions that are useful 
if you need to keep track of more variables than the given parameters, or if you need to change the value of the input.
"""

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return helper(index+1)
    return helper(2)