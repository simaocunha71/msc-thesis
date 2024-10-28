def sequence(n):
    a = 1
    b = 1
    for _ in range(n-2):
        a, b = b, max(a, b) + 1
    return b