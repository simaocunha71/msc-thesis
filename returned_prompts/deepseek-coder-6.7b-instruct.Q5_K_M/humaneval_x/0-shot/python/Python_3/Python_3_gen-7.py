from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([100, -50, -75]))  # True
print(below_zero([10, -10, -20, 30]))  # False
print(below_zero([0, 100, -50, -25]))  # True

This function iterates over each operation in the operations list. It adds the value of the operation to the current balance. If at any point the balance is less than zero, the function returns True. If it goes through all operations without finding a balance less than zero, the function returns False.

The time complexity of this function is O(n), where n is the number of operations. This is because it performs a single operation for each operation in the input list. The space complexity is O(1), which means the memory used does not grow with the size of the input list.

This function assumes that the input is a list of integers representing the deposit and withdrawal operations on a bank account. It does not handle any exceptions or errors that might occur if the input is not in the expected format.

This function should work correctly for all possible inputs, as long as the input is a list of integers. If you need to handle other types of inputs, you will need to add additional error checking.

This function is not optimized for performance, and it could be made more efficient by using a generator to perform the operations and checking the balance at the same time.
"""

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([100, -50, -75]))  # True
print(below_zero([10, -10, -20, 30]))  # False
print(below