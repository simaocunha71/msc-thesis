def jacobsthal_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return jacobsthal_num(n-1) + 2*jacobsthal_num(n-1) - jacobsthal_num(n-2)  # Recursive formula for Jacobsthal numbers. 