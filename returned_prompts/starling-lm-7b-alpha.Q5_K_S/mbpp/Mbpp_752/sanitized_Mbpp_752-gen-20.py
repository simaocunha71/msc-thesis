def jacobsthal_num(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (2 * jacobsthal_num(n-2) + jacobsthal_num(n-1)) % 1000000007