class Account:
    bank_name = "Equity Bank"
    def __init__(self, account_number, account_name, balance):
        # Instance variables
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.deposits = []  
        self.withdrawals = []
        self.loan_balance = 0

    def deposit(self, amount):
        self.balance += amount
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction) 
    def withdrawal(self, amount):
        self.balance -= amount
        transaction = {
            "amount": amount,
            "narration": "withdrawal"
        }
        self.withdrawals.append(transaction)
    def transact(self):
        for transaction in self.deposits: 
            print(transaction)
        for transaction in self.withdrawals:
            print(transaction)
    def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")
    def borrow_loan(self,loan_amount):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if self.loan_balance==0 and loan_amount>100 and len(self.deposits)>=10 and loan_amount > total_deposits / 3:
           return
        self.loan_balance+=loan_amount
        self.balance+=loan_amount
    def repay_loan(self,amount):
        self.loan_balance-=amount
        if amount>self.loan_balance:
            extra=self.loan_balance-amount
            self.balance+=extra
    def transfer(self,amount,other_account):
        other_account=Account
        if self.balance> amount:
            return
        self.balance -= amount
        other_account.check_deposit

        
    

acc1 = Account('233465', 'Veronica', 0)
acc1.deposit(66)
acc1.withdrawal(100)
acc1.transact()

# Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500



# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
# Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500

