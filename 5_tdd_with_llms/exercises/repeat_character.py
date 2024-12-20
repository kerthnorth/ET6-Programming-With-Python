""" Repeat Character

Write a function that takes in a string, a single character, and a number. 
The function returns a string with each occurrence of the character repeated n times.

"""
def repeat_character(item_string, item_char, item_number):
  # item_string = input("Enter a string: ")
  # item_char = input("Enter a character: ")
  # item_number = int(input("Enter a number: "))
  new_string = item_string.lower()
  new_item = item_char.lower()
  result = ""
  for item_character in new_string:
    if item_character == new_item:
      # print(item_char * item_number, end="")
      result += new_item * item_number
    else:
      # print(item_character, end="")
      result += item_character
      
  return result
  # pass

# repeat_character()
