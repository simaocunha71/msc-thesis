    # Initialize
    a, b, c = 0, 0, 1

    # Iterate
    for _ in range(n):
        a, b, c = b, c, a + b + c

    return a


