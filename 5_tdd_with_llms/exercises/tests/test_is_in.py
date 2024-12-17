import unittest
from is_in import *

class TestIsIn(unittest.TestCase):
  def test_is_in_both(self):
    
    self.assertEqual(is_in("a", ["a", "b"], ["a", "c"]), True)
    
  def test_is_not_in_both(self):
    self.assertEqual(is_in("z", ["a", "b"], ["a", "c"]), False)
    
  def test_is__in_one(self):
    self.assertEqual(is_in("b", ["a", "b"], ["a", "c"]), True)
