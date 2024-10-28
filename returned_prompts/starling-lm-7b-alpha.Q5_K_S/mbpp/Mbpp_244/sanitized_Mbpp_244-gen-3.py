def next_Perfect_Square(n):
    sqrt_n = int(n ** 0.5) + 1
    while True:
        if (sqrt_n ** 2) > n:
            return (sqrt_n ** 2)
        else:
            sqrt_n += 1