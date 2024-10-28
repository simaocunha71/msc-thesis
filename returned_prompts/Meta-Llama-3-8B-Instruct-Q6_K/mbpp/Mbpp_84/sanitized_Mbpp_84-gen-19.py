def sequence(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        a, b, c = 1, 1, 2
        for _ in range(4, n + 1):
            a, b, c = b, c, a + b
        return c