#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution. 
The following code attempts to calculate the nth number in the Fibonacci sequence.

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

Parameters:
- n (int): The position in the Fibonacci sequence.
- memo (dict): This is a dictionary to store computed Fibonacci values for reuse.

Returns:
- int: The nth Fibonacci number.

Test Cases:
- fibonacci(0) should return 0.
- fibonacci(1) should return 1.
- fibonacci(5) should return 5.
- fibonacci(10) should return 55.
"""


def fibonacci(n: int, memo: dict = {}) -> int:
    """


    base case 1:

    base case 2:

    base case 3:

    recursive case:

    """
    if n == 0: # This is a base case
        return 0 # if n value is 0, return 0

    if n == 1: # This is a base case too
        return 1 # if n value is 1, return 1

    if n in memo: # This is a base case
        return memo[n] # if n value is in memo, return memo
    
    # this is a recursive case that operates from the left side
    left_recursion = fibonacci(n - 1, memo)
    # this is a recursive case that operates from the right side
    right_recursion = fibonacci(n - 2, memo)
    # the results are stored in memo
    memo[n] = left_recursion + right_recursion
    
    # return memo[n]
    print(memo[n])
fibonacci(5)


# --- --- --- test cases --- --- ---

# write some test cases!
print(fibonacci(0) , 'should be ', 0)
print(fibonacci(1) , 'should be ', 1)
print(fibonacci(5) , 'should be ', 5)
print(fibonacci(10) , 'should be ', 55)
