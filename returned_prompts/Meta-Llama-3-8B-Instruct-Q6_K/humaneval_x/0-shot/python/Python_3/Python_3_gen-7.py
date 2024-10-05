from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
# test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([1, 1, 1, 1, 1]))  # False
print(below_zero([-1, -1, -1, -1, -1]))  # True
print(below_zero([1, 2, 3, 4, 5]))  # False
print(below_zero([1, 2, 3, -4, 5]))  # True
print(below_zero([1, 2, -3, 4, 5]))  # True
print(below_zero([1, -2, 3, 4, 5]))  # True
print(below_zero([-1, 2, -3, 4, 5]))  # True
print(below_zero([1, 2, -3, -4, 5]))  # True
print(below_zero([1, 2, 3, 4, -5]))  # True
print(below_zero([1, 2, 3, -4, -5]))  # True
print(below_zero([-1, 2, -3, -4, 5]))  # True
print(below_zero([1, -2, 3, -4, 5]))  # True
print(below_zero([-1, -2, 3, -4, 5]))  # True
print(below_zero([1, 2, 3, 4, 5]))  # False
print(below_zero([-1, -2, -3, -4, -5]))  # True
print(below_zero([1, 2, 3, -4, -5]))  # True
print(below_zero([1, 2, 3, 4, -5, -6]))  # True
print(below_zero([1, 2, 