def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (jacobsthal_num(n-1) + jacobsthal_num(n-2)) * (n + 1)


def jacobsthal_num_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num_recursive(n-1) * (n + 1) + jacobsthal_num_recursive(n-2) * (n + 1)
