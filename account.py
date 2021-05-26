# @Author: junoh26

class Account:

    def __init__(self, cardId, PIN, balance=0):
        self.cardId = cardId
        self.PIN = PIN
        self.balance = balance

    def __eq__(self, other):
        return self.cardId == other.cardId and self.PIN == other.PIN \
            and self.balance == other.balance
    
    def getCardId(self):
        return self.cardId

    def getPIN(self):
        return self.PIN
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount 