def jacobsthal_num(n):
    """
    Returns the nth jacobsthal number
    >>> jacobsthal_num(5)
    11
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return 2*jacobsthal_num(n-1) + jacobsthal_num(n-2) + jacobsthal_num(n-3)