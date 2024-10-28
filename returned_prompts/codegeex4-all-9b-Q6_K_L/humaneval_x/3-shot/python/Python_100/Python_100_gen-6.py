    if n % 2 == 0:
        return list(range(n, n + 2 * (n - 1), 2))
    else:
        return list(range(n, n + 2 * (n - 1) + 1, 2))

