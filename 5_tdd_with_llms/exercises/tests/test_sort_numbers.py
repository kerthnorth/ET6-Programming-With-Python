import unittest
from sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):
  def test_sort_numbers(self):
    """Test case 1: List with numbers"""
    lst = [5, 4, 3, 2, 1]
    result = sort_numbers(lst)
    expected = [1, 2, 3, 4, 5]
    self.assertEqual(result, expected)
    
  def test_empty_list(self):
    """Test case 2: Empty list"""
    lst = []
    result = sort_numbers(lst)
    expected = []
    self.assertEqual(result, expected)
