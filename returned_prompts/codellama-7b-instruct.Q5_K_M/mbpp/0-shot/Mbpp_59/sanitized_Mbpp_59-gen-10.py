def is_octagonal(n):
    n_squared = n * n
    root = int(n_squared ** 0.5)
    return root * (root + 1) == n_squared