class Account:
    def __init__(self):
        self._balance=0
    @property
    def balance(self):
        return self._balance
    def __str__(self):
        return f"{self.balance}"
    def deposit(self, n):
        self._balance+=n
    def withdraw(self,n):
        self._balance-=n

def main():
    balance=Account()
    print(balance.balance)
    balance.deposit(101)
    balance.withdraw(14)
    print(balance.balance)

main()
