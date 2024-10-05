    factors = []
    n_copy = n
    for i in range(2, n + 1):
        while n_copy % i == 0:
            factors.append(i)
            n_copy //= i

    return factors

