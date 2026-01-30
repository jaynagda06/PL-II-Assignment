class Bank:
    def __init__(self, pin, account_number, balance):
        self.pin = pin
        self.account_number = account_number
        self.balance = balance

    def verify(self, mpin, account_number):
        return self.pin == mpin and self.account_number == account_number

    def deposit(self, mpin, account_number, amount):
        if self.verify(mpin, account_number):
            self.balance += amount
            print("Updated Balance:", self.balance)
        else:
            print("Wrong Pin or Account Number.")

    def withdraw(self, mpin, account_number, amount):
        if self.verify(mpin, account_number) and self.balance >= amount:
            self.balance -= amount
            print("Updated Balance:", self.balance)
        else:
            print("Wrong Pin or Insufficient Balance.")

    def check_balance(self, mpin, account_number):
        if self.verify(mpin, account_number):
            print(self.balance)
        else:
            print("Wrong Pin or Account Number.")


pin = int(input("Enter pin: "))
account_number = int(input("Enter account number: "))
balance = int(input("Enter balance: "))
bank = Bank(pin, account_number, balance)

while True:
    choice = int(input(
        "1.Deposit\n"
        "2.Withdraw\n"
        "3.Check balance\n"
        "Choose anyone for operation: "
    ))

    mpin = int(input("Enter pin: "))
    acc_no = int(input("Enter account number: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        bank.deposit(mpin, acc_no, amount)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        bank.withdraw(mpin, acc_no, amount)
    elif choice == 3:
        bank.check_balance(mpin, acc_no)
    else:
        print("Invalid Choice.")

    op = input("Enter (Y/y) to continue or (N/n) to stop: ")
    if op.lower() != 'y':
        break
