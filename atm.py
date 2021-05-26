# @Author: junoh26

class Atm:
    
    def __init__(self, userAccounts):
        self.userAccounts = userAccounts

    def getAccounts(self):
        return self.userAccounts

    def insertCard(self, cardId):
        userAcc = None
        for account in self.userAccounts:
            if cardId == account.getCardId():
                userAcc = account
                break
        return userAcc

    def insertPIN(self, cardId, PIN):
        for account in self.userAccounts:
            if cardId == account.getCardId() and PIN == account.getPIN():
                return True
            elif cardId == account.getCardId() and PIN != account.getPIN():
                return False
        return False
