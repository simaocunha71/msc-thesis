def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)