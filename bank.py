class Bank:
    bank_name = "Equity Bank"
    
    def __init__(self, account_holder, account_name, balance):
        # Instance variables
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Your deposit is successful.Your new balance is {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal was successful and your new balance is  {self.balance}")
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.balance