""" Is in

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _at least one_ of the lists.

"""
def is_in(item, list1, list2):
  #  I will create a condition that checks if the item is in either list
  if item in list1 or item in list2:
    # it prints true for debugging purposes and returns us the result
    print("True")
    return True
  # if the item is not in either list, it returns false
  print("False")
  return False
