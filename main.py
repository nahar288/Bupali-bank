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

while True:

    print("===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Set Balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "4":
        amount = float(input("Enter new balance: "))
        account.set_balance(amount)

    elif choice == "5":
        print("dhonnobash🤑")
        break

    else:
        print("Invalid option. Please choose 1-5.")