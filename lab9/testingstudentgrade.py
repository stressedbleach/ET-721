"""
SIMRIDHI SHARMA
sep 30
unit testing input data
"""

import unittest
from unittest.mock import patch
import io
import studentgrade

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '85', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        # Call main function
        studentgrade.main()

        # Capture printed output
        output = mock_stdout.getvalue()

        # Check output contains the correct average
        self.assertIn("The class average is 83.33\n", output)  # Average of 85, 90, 75

    @patch('builtins.input', side_effect=['-1', '2', '-5', '85', '101', '90'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        # Call main function
        studentgrade.main()

        # Capture printed output
        output = mock_stdout.getvalue()

        # Check output contains the error messages
        self.assertIn("Invalid input.\n", output)  # For invalid number of students
        self.assertIn("Grade must be between 0 and 100\n", output)  # For invalid grades
        self.assertIn("The class average is 87.50\n", output)  # Correct average of valid grades

    @patch('builtins.input', side_effect=['Peter', '3', '85', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_student_count_string(self, mock_stdout, mock_input):
        # Call main function
        studentgrade.main()

        # Capture printed output
        output = mock_stdout.getvalue()

        # Check output contains the error message for invalid input
        self.assertIn("Invalid input, try again.\n", output)  # For string input instead of int

    @patch('builtins.input', side_effect=['3', 'Peter', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_grade_string(self, mock_stdout, mock_input):
        # Call main function
        studentgrade.main()

        # Capture printed output
        output = mock_stdout.getvalue()

        # Check output contains the error message for invalid grade input
        self.assertIn("Invalid input.\n", output)  # For string input instead of int

if __name__ == "__main__":
    unittest.main()

