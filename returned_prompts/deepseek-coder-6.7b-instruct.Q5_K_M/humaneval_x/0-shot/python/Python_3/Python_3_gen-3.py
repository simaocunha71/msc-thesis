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
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, -2, 3]))  # True
print(below_zero([1, 2, -5]))  # True
print(below_zero([1, 2, 3, -7]))  # True
print(below_zero([1, 2, 3, 4, -10]))  # False

This function works by maintaining a running total of the balance. For each operation, it adds the amount to the balance, then checks if the balance is now less than zero. If it is, the function immediately returns True. If no operation makes the balance negative, the function returns False after going through all the operations.

This solution has a time complexity of O(n) where n is the number of operations, because it performs a single pass over the operations. The space complexity is O(1), because it only uses a single integer to keep track of the balance.
