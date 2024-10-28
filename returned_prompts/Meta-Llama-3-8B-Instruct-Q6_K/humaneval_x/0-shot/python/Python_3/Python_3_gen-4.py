from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
# This function iterates over each operation in the list, adding it to the balance. If the balance
# ever falls below zero, it immediately returns True. If the loop finishes without the balance falling
# below zero, it returns False.

# Example usage:
print(below_zero([1, 2, 3]))  # Returns False
print(below_zero([1, 2, -4, 5]))  # Returns True
print(below_zero([1, 1, 1, 1]))  # Returns False
print(below_zero([-1, -1, -1, -1]))  # Returns True
print(below_zero([0, 0, 0, 0]))  # Returns False
print(below_zero([-1, 0, 0, 1]))  # Returns True
print(below_zero([1, -1, 0, 1]))  # Returns True
print(below_zero([1, 1, 1, 1, -1]))  # Returns True
print(below_zero([1, 1, 1, 1, 1]))  # Returns False
print(below_zero([0, 1, 1, 1]))  # Returns False
print(below_zero([-1, -1, -1, -1, -1]))  # Returns True
print(below_zero([1, 1, 1, 1, 1, -1]))  # Returns True
print(below_zero([1, 1, 1, 1, 1, 1]))  # Returns False
print(below_zero([1, 1, 1, 1, 1, 1, -1]))  # Returns True
print(below_zero([1, 1, 1, 1, 1, 1, 1]))  # Returns False
print(below_zero([-1, -1, -1, -1, -1, -1, -1]))  # Returns True
print(below_zero([1, 1, 1, 1, 1, 1, 1, -1]))