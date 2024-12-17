import unittest
from sum_evens_and_odds import check_number
class TestCheckNumber(unittest.TestCase):
    def test_check_number_default(self):
        """Test case 1: Default list of numbers"""
        result = check_number()
        expected = {"even": 30, "odd": 25}
        self.assertEqual(result, expected)
