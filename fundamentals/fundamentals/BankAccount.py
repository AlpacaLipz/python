class BankAccount:
    def __init__ (self, intrest_rate, balance):
        self.balance = balance
        self.intrest_rate = intrest_rate

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance = self.balance - 5
        return self
        
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.blanace = self.balance * self.intrest_rate
        return self

account1 = BankAccount(.05, 500)
account2 = BankAccount(.1, 1000)

account1.deposit(25).deposit(10).deposit(30).withdraw(100).yield_intrest().display_account_info()
account2.deposit(100).deposit(500).withdraw(100).withdraw(100).withdraw(500).withdraw(100).yield_intrest().display_account_info()