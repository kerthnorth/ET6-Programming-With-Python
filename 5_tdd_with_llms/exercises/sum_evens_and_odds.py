""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""
def check_number():
  odd_num =[]
  even_num =[]
  num_list = [1,2,3,4,5,6,7,8,9,10]

  for num in num_list:
    if num % 2 == 0:
      even_num.append(num)
    else:
      odd_num.append(num)
      
  print(even_num)
  print(odd_num)

  return {"even": sum(even_num), "odd": sum(odd_num)}
check_number()
