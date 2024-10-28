def find_lucas(n):
    if n <= 2:
        if n == 1:
            return 2
        elif n == 2:
            return 1
    else:
        a, b = 2, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    return None