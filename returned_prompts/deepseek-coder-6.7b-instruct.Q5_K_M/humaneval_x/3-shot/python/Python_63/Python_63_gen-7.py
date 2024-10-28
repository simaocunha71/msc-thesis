    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c

    return c


