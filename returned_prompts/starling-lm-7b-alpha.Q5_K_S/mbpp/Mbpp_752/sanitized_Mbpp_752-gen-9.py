def jacobsthal_num(n):
    """
    The nth Jacobsthal number is given by the formula:
        J(n) = 2 * J(n-1) + 2 * J(n-2) - 1
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return 2 * jacobsthal_num(n-1) + 2 * jacobsthal_num(n-2) - 1