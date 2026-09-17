class BankAccount:

    def __init__(self, account_number, account_holder, initial_balance: float=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance
   
    def get_balance(self):
        return self.__balance

    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal")
  
    def check_balance(self):
        print(f"Balance: ${self.get_balance()}")


account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder, initial_balance)

