from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 5, -10]))  # True
print(below_zero([5, 5, 5, 5]))  # False
print(below_zero([-5, -5, -5, -5]))  # True
print(below_zero([1, 2, 3, 4, 5]))  # False
print(below_zero([-1, -2, -3, -4, -5]))  # True
print(below_zero([10, 10, 10, 10, 10]))  # False
print(below_zero([-10, -10, -10, -10, -10]))  # True
print(below_zero([10, 10, -10, 10, -10]))  # True
print(below_zero([10, -10, 10, 10, -10]))  # True
print(below_zero([10, -10, -10, 10, 10]))  # True
print(below_zero([10, -10, 10, -10, 10]))  # True
print(below_zero([10, -10, -10, -10, -10]))  # True
print(below_zero([10, 10, 10, 10, 10, 10]))  # False
print(below_zero([-10, -10, -10, -10, -10, -10]))  # True
print(below_zero([10, -10, 10, -10, 10, -10]))  # True
print(below_zero([10, 10, -10, -10, 10, -10]))  # True
print(below_zero([10, 10, 10, -10, 10, -10]))  # True
print(below_zero([10, 10, 10, 10, -10, -10]))  # True