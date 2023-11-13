from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

    # if balance is not zero then it will be too big as soon as first operation happens
    # or if we're left with an amount of money to pay for the operations that have been performed.
    def get_balance(operations: List[int]) -> int:
        """
        It just calculates balance, assuming it was zero before any operations happened.
        """
        # balace can never be negative, because at least one operation will set the amount to 0
        if not operations:
            return 0
        elif len(operations) > 1 and (operations[-1] < 0 or operations[0] < 0):
            return get_balance([-operations[-1], -operations[0]])
        else:
            return operations[-1] if operations else 0