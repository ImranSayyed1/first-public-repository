# difference between static and non-static variable and method in Python

class Account:
    name=" "
    balance=" "
    rate=9        # static  member or class variable

    def __init__(self,name,balance):
        self.name=name          # non-static or instance member
        self.balance=balance    # non-static or instance member
    def getname(self):
        return self.name
    def getbalance(self):
        return self.balance

    @staticmethod
    def getrate():
        return Account.rate

a1= Account("Ramesh",50000)
print(a1.getname())
print(a1.getbalance())
print(Account.getrate())

