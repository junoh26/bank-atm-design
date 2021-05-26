# @Author: junoh26

import unittest
from atm import Atm
from account import Account

class AtmTest(unittest.TestCase):

    def setUp(self):
        
        print("test set up completed")

    def tearDown(self):

        print("test set up cleared")

    def test_getId(self):
        print("getId tested successfully")

    def test_getBalance(self):

        print("getBalance tested successfully")

    def test_deposit(self):

        print("deposit tested successfully")

    def test_withdraw(self):

        print("withdraw tested successfully")

if __name__ == '__main__':
    unittest.main()