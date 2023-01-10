# difference between static and non-static variable in Python

class Account:
    name = " "
    balance = " "
    rate = 9  # static  member or class variable

    def __init__(self, name, balance):
        self.name = name  # non-static or instance member
        self.balance = balance  # non-static or instance member


a1 = Account("Ramesh", 50000)
print(getattr(a1, 'name'))
print(getattr(a1, 'balance'))
print(getattr(Account, 'rate'))
