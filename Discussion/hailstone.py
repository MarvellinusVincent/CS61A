"""
Q4: Recursive Hailstone
Recall the hailstone function from Homework 2. First, pick a positive integer n as the start. 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. 
Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.

Hint: When taking the recursive leap of faith, consider both the return value and side effect of this function.
"""

def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return m + (multiply (m, n-1))