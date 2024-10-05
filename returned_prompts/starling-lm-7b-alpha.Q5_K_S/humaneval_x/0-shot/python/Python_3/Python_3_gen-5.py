    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

# Below zero
# You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance. Your task is to detect if at any point the balance of account fallls below zero, and at that point function should return True. Otherwise it should return False.

# >>> below_zero([1, 2, 3])
# False
# >>> below_zero([1, 2, -4, 5])
# True


def below_zero(operations: List[int]) -> bool:
    """
    :param operations: List of deposit and withdrawal operations
    :return: True if at any point the balance of account fallls below zero, otherwise False
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


if __name__ == '__main__':
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True


# Below zero
# You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance. Your task is to detect if at any point the balance of account fallls below zero, and at that point function should return True. Otherwise it should return False.

# >>> below_zero([1, 2, 3])
# False
# >>> below_zero([1, 2, -4, 5])
# True


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


if __name__ == '__main__':
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True


# Below zero
# You're given a list of deposit and withdrawal operations on a bank account