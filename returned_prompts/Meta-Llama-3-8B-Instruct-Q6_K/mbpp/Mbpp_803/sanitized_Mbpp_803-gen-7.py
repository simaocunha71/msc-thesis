def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = n ** 0.5
    return int(sqrt + 0.5) ** 2 == n