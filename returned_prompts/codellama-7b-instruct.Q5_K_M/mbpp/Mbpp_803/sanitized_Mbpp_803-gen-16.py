def is_perfect_square(n):
    s = 0
    while s * s <= n:
        s += 1
    return s * s == n