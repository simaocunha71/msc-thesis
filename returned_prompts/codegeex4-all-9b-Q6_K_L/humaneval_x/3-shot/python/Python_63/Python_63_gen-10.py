    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

