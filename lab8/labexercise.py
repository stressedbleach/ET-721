"""
Simridhi sharma
lab exercise
"""

import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("John Doe", 100)  # Assume account starts with a balance of 100

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        self.account.deposit(50)
        print(f"Balance after depositing 50: {self.account.balance}")
        self.assertEqual(self.account.balance, 150)

    def test_withdrawal(self):
        self.account.withdraw(30)
        print(f"Balance after withdrawing 30: {self.account.balance}")
        self.assertEqual(self.account.balance, 70)

    def test_overdraw_exception(self):
        with self.assertRaises(ValueError):  # Assuming BankAccount raises ValueError on overdraw
            self.account.withdraw(200)
        print("Overdraw attempt raised ValueError as expected.")

    def test_sequence_of_operations(self):
        self.account.deposit(100)
        print(f"Balance after depositing 100: {self.account.balance}")
        self.account.withdraw(50)
        print(f"Balance after withdrawing 50: {self.account.balance}")
        self.account.deposit(25)
        print(f"Final balance after depositing 25: {self.account.balance}")
        self.assertEqual(self.account.balance, 175)

if __name__ == '__main__':
    unittest.main()
