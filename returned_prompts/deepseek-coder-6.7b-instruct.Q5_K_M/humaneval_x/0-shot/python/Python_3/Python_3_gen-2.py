from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True

Explanation:
The function below_zero() accepts a list of operations. For each operation, it adds the operation to the current balance. If the balance is less than zero at any point, the function returns True. If no operation causes the balance to fall below zero, the function returns False.
"""


"""
