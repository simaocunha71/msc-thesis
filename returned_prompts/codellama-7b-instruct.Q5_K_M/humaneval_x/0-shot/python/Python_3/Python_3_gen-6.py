
class Account:

    def __init__(self) -> None:
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

    def below_zero(self) -> bool:
        return self.balance < 0


operations = [1, 2, -4, 5]

account = Account()
for op in operations:
    if op < 0:
        account.withdraw(op)
    else:
        account.deposit(op)

print(account.below_zero())