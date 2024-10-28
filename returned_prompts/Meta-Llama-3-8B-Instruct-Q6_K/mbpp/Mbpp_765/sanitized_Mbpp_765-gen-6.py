def is_polite(n):
    i = 0
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        if a > n:
            return b
        i += 1
        if i == n:
            return a