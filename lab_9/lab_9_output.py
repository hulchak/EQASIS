class Customer:
    def __init__(self, account):
        self.account = account

    def get_balance(self):
        return self.account.get_balance()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, customer):
        self.customer = customer

    def get_balance(self):
        return self.customer.get_balance()

# Користування спрощеним ланцюжком викликів
bank = Bank(Customer(Account(1000)))
balance = bank.get_balance()
print(f"The balance is: {balance}")
