""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""

def is_in_both(item, list1, list2):
    # I create a condition that checks if the item is in both lists
    if item in list1 and item in list2: 
        # it prints true for debugging purposes and returns us the result
        print("True")
        return True
    # if the item is not in both lists, it returns false
    print("False")
    return False

# is_in_both()
