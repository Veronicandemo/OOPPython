class Account:
    bank_name = "Equity Bank"
    
    def __init__(self, account_number, account_name, balance):
        # Instance variables
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f'Your deposit is successful.Your new balance is {self.balance}'
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f'Withdrawal was successful and your new balance is  {self.balance}'
        else:
           return f'Insufficient funds.Please add funds to withdraw'
    
    def get_balance(self):
        return self.balance