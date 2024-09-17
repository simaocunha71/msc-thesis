def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        n -= 2
        a, b = 1, 1
        for _ in range(n):
            a, b = b, (2*a+b)%2
        return b