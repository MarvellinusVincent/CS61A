""""
Q1: Warm Up: Recursive Multiplication
These exercises are meant to help refresh your memory of the topics covered in lecture.

Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers. 
Use recursion, not mul or *.

Hint: 5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).
"""

def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    return m + (multiply (m, n-1))