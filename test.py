# @Author: junoh26

import unittest
from atm import Atm
from account import Account

class AtmTest(unittest.TestCase):

    def setUp(self):
        userAccounts = [Account(10000001, 1), Account(10000002, 2), Account(10000003, 3)]
        self.atm = Atm(userAccounts)

    def tearDown(self):
        self.atm = Atm()

    # In case cardId exists in bank
    def test_insert_card_1(self):
        cardId = 10000002
        userAcc = self.atm.insertCard(cardId)
        self.assertNotEqual(userAcc, None)
    
    # In case cardId doesn't exist in bank
    def test_insert_card_2(self):
        cardId = 99999999
        userAcc = self.atm.insertCard(cardId)
        self.assertEqual(userAcc, None)

    # PIN number is correct
    def test_insert_pin_1(self):
        cardId, PIN = 10000002, 2
        valid = self.atm.insertPIN(cardId, PIN)
        self.assertEqual(valid, True)

    # PIN number is incorrect
    def test_insert_pin_2(self):
        cardId, PIN = 10000002, 5555
        valid = self.atm.insertPIN(cardId, PIN)
        self.assertEqual(valid, False)


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account(10000001, 1, 50)

    def tearDown(self):
        self.account = None

    def test_getCardId(self):
        self.assertEqual(self.account.getCardId(), 10000001)

    def test_getBalance(self):
        self.assertEqual(self.account.getBalance(), 50)

    # 50 + 30 = 80
    def test_deposit(self):
        self.account.deposit(30)
        self.assertEqual(self.account.getBalance(), 80)

    # 50 - 30 = 20
    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.getBalance(), 20)

if __name__ == '__main__':
    unittest.main()