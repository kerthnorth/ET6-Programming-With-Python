import unittest
from is_in_both import * # type: ignore

"""

Writing test that checks if a string is in either of the lists
It will return true if the item is in _both_ of the lists.
it will return false if not
"""
class TestIsInBoth(unittest.TestCase):
  def test_is_in_both(self):
    
    self.assertEqual(is_in_both("a", ["a", "b"], ["a", "c"]), True)
    
  def test_is_not_in_both(self):
    self.assertEqual(is_in_both("z", ["a", "b"], ["a", "c"]), False)
