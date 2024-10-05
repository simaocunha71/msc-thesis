    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


