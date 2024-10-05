    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


# Run tests
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True


# More tests
print(below_zero([1, 2, -4, -5]))  # True
print(below_zero([10, 20, -30]))  # True
print(below_zero([100, 200, 300]))  # False


def sum_operations(operations: List[int]) -> int:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts
    with zero balance. Your task is to calculate the total sum of deposit and withdrawal operations.
    >>> sum_operations([1, 2, 3])
    6
    """
    return sum(operations)


# Run tests
print(sum_operations([1, 2, 3]))  # 6
print(sum_operations([1, 2, -4, 5]))  # 4
print(sum_operations([1, 2, -4, -5]))  # -3
print(sum_operations([10, 20, -30]))  # 10
print(sum_operations([100, 200, 300]))  # 400


# More tests
print(sum_operations([100, 200, 300, -400, 500]))  # 200
print(sum_operations([10000, -20000, 30000, -50000, 60000]))  # 10000


def below_zero_and_sum(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts
    with zero balance. Your task is to detect if at any point the balance of account falls