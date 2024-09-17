def is_nonagonal(n):
    a, b = 1, 8
    for _ in range(n - 1):
        a, b = b, a + b
    return b