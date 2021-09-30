# Create a unit test method to test the calculate_avg function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest

from app.src.utils import calculate_avg


class TestUtils(unittest.TestCase):

    def test_calc_avg_valid(self):

        input = [3,1,2,99,5]
        actual = calculate_avg(input)
        expect = 22
        self.assertEqual(expect, actual)
        self.assertTrue(isinstance(actual,float))

    def test_bad_input_type(self):
        input = ['s', 'f']
        self.assertRaises(TypeError, calculate_avg, input)
        


    def test_calc_avg_empty_list(self):
        self.assertRaises(Exception, calculate_avg, [])