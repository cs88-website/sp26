class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account.deposit()
    - decreased by account.withdraw()
    """

    # Constructor
    def __init__(self, name, initial_deposit=0, account_number=0, bank=None):
        # Initialize the instance attributes
        self._name = name
        self._bank = bank
        self.__acct_no = account_number
        self.__balance = initial_deposit

    # Selectors
    def account_name(self):
        return self._name

    # Unnecessary short-hand.
    def balance(self):
        return self.account_balance()

    def account_balance(self):
        return self.__balance

    def account_number(self):
        return self.__acct_no

    # Operations
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def account_type(self):
        return "Base"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}Account: {self.account_name()}-{self.account_number()} Balance: {self.account_balance()}'

    # This is only useful for debugging.
    def show_superclass(self):
        return super()

class CheckingAccount(BaseAccount):

    def __init__(self, name, initial_deposit, account_number=0, bank=None):
        # Use superclass initializer
        BaseAccount.__init__(self, name, initial_deposit, account_number, bank)
        # Alternatively, recommended:
        # super().__init__(name, initial_deposit, account_number, bank)
        # Additional initialization

    def withdraw(self, amount):
        """
        Adapt the withdraw methods to prevent "overdrafting"
        """
        if self.account_balance() - amount < 0:
            return "ERROR: You are not allowed to overdraft a CheckingAccount."
        # BaseAccount.withdraw(self, amount)
        return super().withdraw(amount)

    def account_type(self):
        return "Checking"

    # Just for debugging / example:
    def show_superclass(self):
        return super()

class SavingsAccount(BaseAccount):
    interest_rate = 0.02

    def __init__(self, name, initial_deposit, account_number=0, bank=None):
        # Use superclass initializer
        super().__init__(name, initial_deposit, account_number, bank)

    def accrue_interest(self):
        # We should use `self.interest_rate` so the RetirementSavingsAccount works
        self.__balance = self.__balance * (1 + self.interest_rate)

    def account_type(self):
        return "Savings"
    # Display representation
    def __repr__(self):
        # Alternatively, we can use `type(self)` to infer the class.
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()} @ {type(self).interest_rate * 100}%>'


class RetirementSavingsAccount(SavingsAccount):
    interest_rate = 0.05
    # No __init__ here
    def withdraw(self, amount):
        return f"ERROR: You cannot withdraw from a {self.account_type()}."

    def account_type(self):
        return "RetirementSavings"

class Bank:
    def __init__(self, name, initial_account_number=1000):
        self.name = name
        self.__next_account_no = initial_account_number
        self.__accounts = []

    def new_account(self, name, initial_deposit=0, account_type=CheckingAccount):
        account_no = self.__next_account_no
        account = account_type(name, initial_deposit, account_no, self)
        self.__next_account_no += 1
        self.__accounts.append(account)
        return account

    def show_accounts(self):
        for acct in self.__accounts:
            print(acct)

    def all_accounts(self):
        return tuple(self.__accounts)

    # This allows us to write len(bank)
    def __len__(self):
        return len(self.__accounts)

    def total_assets(self):
        return sum(map(lambda a: a.account_balance(), self.__accounts))

    def __str__(self):
        return f"Bank of {self.name} with {len(self)} accounts."

    def account_types():
        return {
            'Checking': CheckingAccount,
            'Savings': SavingsAccount,
            'RetirementSavings': RetirementSavingsAccount
        }

#berkeley = Bank('UC Berkeley')
#cs88 = berkeley.new_account('CS88', 1000, CheckingAccount)
#cs61a = berkeley.new_account('CS61A', 1, SavingsAccount)

#berkeley.new_account('CS88 Retirement', 1000, RetirementSavingsAccount)

# Now we can find an account:
#retirement = berkeley.all_accounts()[-1]

# What kinds of accounts exist in our bank?
#Bank.account_types()

# c88c = BaseAccount('C88C Base', 1000, 88)
# checking = CheckingAccount('C88C Checking', 1000, 89)
# savings = SavingsAccount('C88C Savings', 20000, 90)
