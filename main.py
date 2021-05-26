# @Author: junoh26

from atm import Atm
from account import Account

def main():
    
    print("---- ATM activated ----\n")

    # Create accounts to simulate database of user accounts in reality
    accounts = []
    for i in range(9999):
        # Assume that card num is 8-digit and PIN num is 4-digit
        account = Account(i + 10000000, i)
        accounts.append(account)

    # Create Atm obj with user accounts
    atm = Atm(accounts)

    while True:
        
        # User inserts card
        cardId = int(input("Please insert your card ----> "))
        userAcc = atm.insertCard(cardId)

        # Check if card is valid
        if userAcc is None:
            print("**** invalid card ****")
            return
        
        # User enters 4-digit PIN number
        PIN = int(input("Enter 4-digit PIN number: "))

        # Check if PIN is valid
        valid = atm.insertPIN(cardId, PIN)
        if not valid:
            print("**** invalid PIN number ****")
            return

        # Iterate over atm menu options
        while True:

            # Print menu options
            print("\n1. View Balance \t 2. Deposit \t 3. Withdraw \t 4. Exit\n")

            # User selects option
            choice = int(input("Enter your choice: "))

            # View balance
            if choice == 1:
                print("\nYour Current Balance is $" + str(userAcc.getBalance()))

            # Deposit
            elif choice == 2:
                # User enters amount
                amount = int(input("\nEnter amount to deposit: $"))
                userAcc.deposit(amount)
                print("\nYour Current Balance is now $" + str(userAcc.getBalance()))
                print("\n---- Deposit Completed ----")

            # Withdraw
            elif choice == 3:
                # User enters amount
                amount = int(input("\nEnter amount to withdraw: $"))
                currBalance = userAcc.getBalance()
                # Check if user has enough balance
                if currBalance - amount < 0:
                    print("\nNot Enough Balance in your account!\n")
                else:
                    userAcc.withdraw(amount)
                    newBalance = userAcc.getBalance()
                    print("\nYour Current Balance is now $" + str(newBalance))
                    print("\n---- Withdraw Completed ----")

            # Exit
            elif choice == 4:
                print("\n---- Exit ----\n---- Thank you! ----")
                return

if __name__ == '__main__':
    main()
