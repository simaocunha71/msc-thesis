def is_perfect_square(n):
    if n < 0:
        return False
    root = n ** 0.5
    return int(root + 0.5) ** 2 == n