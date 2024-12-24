#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_palindrome(user_in):
    """Return True if the user's input is the same forwards and backwards, otherwise return False.

    :return: True or False
    :rtype: bool
    """
    # user_in = input("Enter a word: ")
    # return user_in == user_in[::-1]
    if user_in == user_in[::-1]:
        # print("True")
        # print(user_in[::-1])
        return True
        
    else:
        # print("False")
        # print(user_in[::-1])
        return False
    
    
check_palindrome()
