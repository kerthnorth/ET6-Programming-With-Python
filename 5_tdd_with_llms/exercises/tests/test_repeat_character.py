import unittest
from repeat_character import *

class TestRepeatCharacter(unittest.TestCase):
  def test_empty_string(self):
    # This test case checks if the user enters an empty string
    self.assertEqual(repeat_character('', '!',  100000000000), "")
    
  def test_zero_repetitions(self):
    # This test case checks if the user enters 0 repetitions
    self.assertEqual(repeat_character('agabani', 'a',  0), "gbni")
    
  def test_case_insensitive_upper_char(self):
    # This test case checks if the user enters an upper case char
    self.assertEqual(repeat_character('Agabani', 'A',  0), "gbni")
    
  def test_case_insensitive_upper_text(self):
    # This test case checks if the user enters an upper case text
    self.assertEqual(repeat_character('Agabani', 'a',  0), "gbni")
    
  def test_case_insensitive_with_non_zero_repetition(self):
    # This test case checks if the user enters a non-zero repetition
    self.assertEqual(repeat_character('Agabani', 'A',  2), "aagaabaani")
    