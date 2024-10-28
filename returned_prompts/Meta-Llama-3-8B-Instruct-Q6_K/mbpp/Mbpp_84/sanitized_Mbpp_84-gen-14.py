def sequence(n):
    if n <= 2:
        return 1 if n == 1 else 2
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b