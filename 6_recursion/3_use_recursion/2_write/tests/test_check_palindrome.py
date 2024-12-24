#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..check_palindrome import check_palindrome


class TestCheckPalindrome(unittest.TestCase):
    def test_empty_string(self):
        """An empty string is a palindrome"""
        self.assertTrue(check_palindrome(""), True)

    def test_single_character(self):
        """A single character is considered a palindrome"""

        self.assertTrue(check_palindrome("a"), True)

    def test_palindrome_even_length(self):
        """A string with an even number of characters that is the same forwards and backwards should return True
        """

        self.assertTrue(check_palindrome("abba"), True)

    def test_palindrome_odd_length(self):
        
        """A string with an odd number of characters that is the same forwards and backwards should return True
        """
        
        self.assertTrue(check_palindrome("madam"), True)

    def test_not_a_palindrome(self):
        
        """A string that is not the same forwards and backwards should return False
        """
        self.assertFalse(check_palindrome("hello"), False)
