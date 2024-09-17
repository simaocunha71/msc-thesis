def jacobsthal_num(n):
    """
    Finds the nth jacobsthal number.

    >>> jacobsthal_num(5)
    11
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2) + jacobsthal_num(n - 3)