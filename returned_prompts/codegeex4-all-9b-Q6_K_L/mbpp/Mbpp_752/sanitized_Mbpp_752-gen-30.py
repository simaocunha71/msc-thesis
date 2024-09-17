def jacobsthal_num(n):
    if n == 0 or n == 1:
        return n
    return 2*jacobsthal_num(n-1) + jacobsthal_num(n-2)