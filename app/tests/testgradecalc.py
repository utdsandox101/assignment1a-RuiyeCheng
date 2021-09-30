# Use unittest library to create a unit test method to test the calculate_avg_grade function created in the gradecalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.Student import Student
from app.src.gradecalc import calculate_avg_grade



class GradeCalculatorTest(unittest.TestCase):

    def test_calculate_average_grade_valid(self):
        input = [
            Student('a', 50, 1, 100.00),
            Student('b', 40, 2, 90.00),
            Student('c', 30, 3, 80.00),
            Student('d', 50, 4, 70.00),
            Student('e', 60, 5, 60.00),
            Student('a', 50, 1, 50.00),
            Student('c', 30, 3, 40.00),
            Student('e', 60, 5, 30.00)
            ]
        expect = {
            1: 75.00,
            2: 90.00,
            3: 60.00,
            4: 70.00,
            5: 45.00
        }
        actual = calculate_avg_grade(input)
        self.assertTrue(isinstance(actual, dict))
        self.assertTrue(len(actual) == 5)
        self.assertFalse(len(actual)==2)
        self.assertEqual(expect, actual)

    def test_calculate_average_grade_empty(self):
        input = {}
        actual = calculate_avg_grade(input)
        self.assertTrue(actual == {})

    def test_calculate_average_grade_bad_input(self):
        input = Student("b","a","d",2)
        self.assertRaises(TypeError, calculate_avg_grade, input)