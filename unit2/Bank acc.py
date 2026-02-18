class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(101, 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
