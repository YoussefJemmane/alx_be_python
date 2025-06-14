
class BankAccount:
    """A simple bank account class that encapsulates banking operations."""
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Deduct the amount from account balance if funds are sufficient.
        Returns True if successful, False if insufficient funds.
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")