from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([5, 5, 5, 5]))  # False
print(below_zero([-1, -2, -3, -4]))  # True
print(below_zero([1, 1, 1, 1, 1]))  # False
print(below_zero([-1, -2, -3, -4, -5]))  # True

# Test cases
assert below_zero([1, 2, 3]) == False
assert below_zero([1, 2, -4, 5]) == True
assert below_zero([5, 5, 5, 5]) == False
assert below_zero([-1, -2, -3, -4]) == True
assert below_zero([1, 1, 1, 1, 1]) == False
assert below_zero([-1, -2, -3, -4, -5]) == True
assert below_zero([]) == False
assert below_zero([0]) == False
assert below_zero([-1]) == True
assert below_zero([1]) == False
assert below_zero([1, 2]) == False
assert below_zero([1, -1]) == True
assert below_zero([1, 2, -1]) == True
assert below_zero([1, -1, 2]) == True
assert below_zero([1, 2, 3, -1]) == True
assert below_zero([1, -1, -1, 1]) == True
assert below_zero([1, 1, 1, 1, 1, -1]) == True
assert below_zero([1, 1, -1, 1, 1]) == True
assert below_zero([1, 1, 1, -1, 1]) == True
assert below_zero([1, 1, -1, -1, 1]) == True
assert below_zero([1, -1,