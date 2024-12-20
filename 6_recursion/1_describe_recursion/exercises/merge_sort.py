#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution. 
The following code attempts to sort a list of numbers using the merge sort algorithm.
we have a base case and a recursive case


"""


def merge_sort(numbers: list) -> list:
    """


    base case:

    recursive case:

    """
    if len(numbers) <= 1:  # This is the base case
        return numbers  # This part returns the base case

    mid = len(numbers) // 2
    # This is a part of the code that handles recursive case. it sorts our program from left to right
    left_half = merge_sort(numbers[:mid])
    # We then merge the sorted halves
    right_half = merge_sort(numbers[mid:])

    return merge(left_half, right_half)


# you do not need to label this helper function
def merge(left, right):
    sorted_numbersay = []
    while left and right:
        if left[0] < right[0]:
            sorted_numbersay.append(left.pop(0))
        else:
            sorted_numbersay.append(right.pop(0))
    sorted_numbersay.extend(left or right)
    return sorted_numbersay


# --- --- --- test cases --- --- ---
print(merge_sort([]), "should be", [])
print(merge_sort([2, 1]), "should be", [1, 2])
print(merge_sort([1, 2, 3]), "should be", [1, 2, 3])
print(merge_sort([5, 3, 8, 6, 2]), "should be", [2, 3, 5, 6, 8])
