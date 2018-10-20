class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Welcome {self.owner}, your current balance is ${self.balance}"

    def deposite(self, amount):
        self.balance += amount
        return f"Deposite accepted. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Funds Unavailable!"
        else:
            self.balance -= amount
            return f"Your new balance is ${self.balance}"
