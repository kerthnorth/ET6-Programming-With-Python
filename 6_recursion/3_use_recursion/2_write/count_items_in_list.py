#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_items_in_list(list_of_things):
    """
    Count the number of items in a list.

    Args:
        list_of_things (list): the list to count

    Returns:
        int: the number of items in the list
    """
    count = 0
    for item in list_of_things:
        count += 1
    # print(count)
    return count
count_items_in_list([1, 2, 3])
