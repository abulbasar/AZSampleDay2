import unittest

from main import AccountType, BankAccount, InvalidAmountException, InsufficientBalanceException

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.acc1 = BankAccount("Test 1", 1000, AccountType.Saving)

    def tearDown(self):
        self.acc1 = None

    def test_withdrawal(self):
        #acc1 = BankAccount("Test 1", 1000, AccountType.Saving)
        acc1 = self.acc1
        acc1.withdraw(100)
        self.assertEqual(900, acc1.amount)

    def test_deposit(self):
        # acc1 = BankAccount("Test 1", 1000, AccountType.Saving)
        acc1 = self.acc1
        acc1.deposit(100)
        self.assertEqual(1100, acc1.amount)

    def test_negative_amount_withdrawal(self):
        # acc1 = BankAccount("Test 1", 1000, AccountType.Saving)
        acc1 = self.acc1
        with self.assertRaises(InvalidAmountException):
            acc1.withdraw(-100)
