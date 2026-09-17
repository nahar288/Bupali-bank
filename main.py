class BankAccount:
    """Simple bank account model."""

    def __init__(self, account_number, account_holder, initial_balance: float = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = 0.0
        self.set_balance(initial_balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a number.")
        if amount < 0:
            print("Balance cannot be negative")
            return False
        self.__balance = float(amount)
        return True
