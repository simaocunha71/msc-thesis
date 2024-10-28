def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True

This function works by iterating over each operation in the operations list. It adds the operation to the balance and checks if the balance is below zero. If it is, the function immediately returns True. If it goes through the entire list without finding a negative balance, the function returns False.

This solution has a time complexity of O(n), where n is the length of the operations list, and a space complexity of O(1), because it only uses a single variable to keep track of the balance.
