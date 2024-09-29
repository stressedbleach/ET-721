"""
Example 3: Verify if the email, full name, and salary fields are correctly formatted
Simridhi sharma
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    

    
    def setUp(self):
        emp1 = Employee("Peter", "Pan", 50000) 


    def test_email(self):
        emp1 = Employee("Peter", "Pan", 50000)
        self.assertEqual(emp1.emailemployee, "Peter.Pan@email.com")

    def test_fullname(self):
        emp1 = Employee("Peter", "Pan", 50000)
        self.assertEqual(emp1.emailemployee, "Peter.Pan@email.com")

    def test_apply_raise(self):
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.salary, 52500)

        

if __name__ == "__main__":
    unittest.main()