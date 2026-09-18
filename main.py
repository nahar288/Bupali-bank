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
  
  


account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder, initial_balance)

while True:

    print("===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Set Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    
    elif choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        amount = float(input("Enter new balance: "))
        account.set_balance(amount)

    elif choice == "4":
        print("dhonnobash🤑")
        break

    else:
        print("Invalid option. Please choose 1-5.")
