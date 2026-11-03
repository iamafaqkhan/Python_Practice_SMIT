import time as t



class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, deposite_amount):

        self.balance = self.balance + deposite_amount

        print(f'Enter amount to deposit: {deposite_amount}')
        print(f'Updated Amount: {self.balance}')

        
    def withdraw(self, withdraw_amount):

        print('--------------------------------')
        print(f'Current amount: {self.balance}')
        print(f'Enter your amount to withdraw: {withdraw_amount}')

        if withdraw_amount > self.balance:
            return 'Insufficient Amount!'

        else: 
            self.balance = self.balance - withdraw_amount
            print(f'Money Remains: {self.balance}')

    def check_balance(self):
        return self.balance

    def money_transfer(self, amount, receiver):

        if amount > self.balance:
            return 'Insufficient To Transfer!'
        else:

            self.balance = self.balance - amount
            print('Processing...')
            t.sleep(3)

            receiver.balance = receiver.balance + amount
            print(f'{amount} transfer to {receiver.account_holder}')


    def display_balance(self):
        print(f'Account Holder: {self.account_holder}')
        print(f'Total Balance in Account: {self.balance}')

        

a1 = BankAccount('John', 1000)
# a1.deposit(50)
# a1.withdraw(20)
# a1.display_balance()
# a1.check_balance()

a2 = BankAccount('Deo', 500)

# a1.money_transfer(200, a2)
a1.money_transfer(300, a2)

a1.display_balance()
# a2.display_balance()








    
