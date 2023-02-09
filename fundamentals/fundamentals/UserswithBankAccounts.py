
#if you read this im really close but i got alot of reading for tomarrow im hoping to finish it up with some help when available im not trying to be dishonest or anything im almost there i know it


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


class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = BankAccount(intrest_rate = 0.05, balance = 1000)



    def make_deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("Insufficient Funds")
        return self
    
    def display_account_info(self):
        print(f"{self.name}")
        print(f"{self.email}")
        print(f"{self.account}")
        return self






User1 = User("Randy Lynd" , "Randy.lynd1988@gmail.com")
User2 = User("Alpaca Jackson", "alpaca.jackson@yourfield.com")
User1.display_account_info()
User2.display_account_info()