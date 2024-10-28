def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
     # This function iterates over the list of operations, adding each operation to the balance.
     # If the balance ever becomes negative, it immediately returns True. If it iterates over the entire list
     # without finding a negative balance, it returns False.