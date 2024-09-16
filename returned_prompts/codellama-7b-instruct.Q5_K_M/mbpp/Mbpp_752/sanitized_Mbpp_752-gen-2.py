def jacobsthal_num(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n % 2 == 0:
        return jacobsthal_num(n/2) + jacobsthal_num(n/2 + 1)
    else:
        return jacobsthal_num(n/2) - jacobsthal_num(n/2 + 1)