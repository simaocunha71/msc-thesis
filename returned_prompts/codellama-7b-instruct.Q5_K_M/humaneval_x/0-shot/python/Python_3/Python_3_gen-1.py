from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


def below_zero_2(operations: List[int]) -> bool:
    """
    >>> below_zero_2([1, 2, 3])
    False
    >>> below_zero_2([1, 2, -4, 5])
    True
    """
    return min(operations) < 0


def below_zero_3(operations: List[int]) -> bool:
    """
    >>> below_zero_3([1, 2, 3])
    False
    >>> below_zero_3([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0


def below_zero_4(operations: List[int]) -> bool:
    """
    >>> below_zero_4([1, 2, 3])
    False
    >>> below_zero_4([1, 2, -4, 5])
    True
    """
    return any(operation < 0 for operation in operations)
