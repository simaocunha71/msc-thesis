def jacobsthal_num(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (2 * jacobsthal_num(n - 1)) + jacobsthal_num(n - 2)