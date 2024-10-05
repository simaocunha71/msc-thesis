from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([100, -150, 50, -100]))  # True
print(below_zero([100, -50, 50, -50]))  # False

Explanation:
We initialize our balance to zero, then iterate through the given list of operations. For each operation, we increase the balance by the operation's value. If at any point the balance is less than zero, we return True. If we finish iterating through the list without finding a balance less than zero, we return False.
"""

# Question 2
"""
