def find_lucas(n):
    if n <= 1:
        return n
    else:
        a, b = 2, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b