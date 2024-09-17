def centered_hexagonal_number(n):
    n -= 1
    a = n * (3 * n + 1) // 2
    b = n * (n + 1)
    c = (n + 1) * (3 * n + 1) // 2
    return a + b + c