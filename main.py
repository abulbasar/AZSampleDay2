
from services import customer_service
from services.customer_service import list_customers

"""
.py file is a module in python
package is special directory that contains one or more module
"""



import traceback

from enum import Enum
# Enum: use enum when you have known set of values for a field.
# For example, banking transaction type (online, mobile, physical banking etc.)
# Status - active, inactive, suspended status

class AccountType(Enum):
    Saving = 1
    Current = 2


class EinextEception(Exception):
    pass


class InsufficientBalanceException(EinextEception):
    pass


class InvalidAmountException(EinextEception):
    pass


class BankAccount:

    def __init__(self, name, amount, account_type):
        self.name = name
        self.__amount = amount
        self.lang = "es"
        if type(account_type) is not AccountType:
            raise Exception("account_type. Expecting AccountTypeEnum")
        self.account_type = account_type

    def __repr__(self):
        return f"Account(name={self.name}, amount={self.amount}, type: {self.account_type})"

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountException()

        if self.__amount < amount:
            raise InsufficientBalanceException("Insufficient amount")

        self.__amount = self.__amount - amount

    def deposit(self, amount):
        self.amount = self.amount + amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise Exception("Negative amount exception")
        self.__amount = value

    def __del__(self):
        print("The object is garbage collected" + str(self))



if __name__ == "__main__":
    acc1 = BankAccount("Elon", 1000, AccountType.Current)
    acc2 = BankAccount("Bill Gates", 2000, AccountType.Current)
    try:
        acc1.withdraw(2000)
    except InsufficientBalanceException as e:
        user_language = acc1.lang
        if user_language == "en":
            message = "Insufficient balance"
        elif user_language == "es":
            message = "Saldo insuficiente"
        print("Transaction failed due to " + message)
        #traceback.print_stack()
        traceback.print_tb(e.__traceback__)
    except InvalidAmountException as e:
        print("Transaction failed due to invalid amount. Please retry." )
        traceback.print_tb(e.__traceback__)

    print("The program is complete !!!")

