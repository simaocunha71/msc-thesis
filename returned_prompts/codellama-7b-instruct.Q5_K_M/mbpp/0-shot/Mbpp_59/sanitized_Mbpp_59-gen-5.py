def is_octagonal(n):
    return is_pentagonal(n) and is_hexagonal(n)
def is_pentagonal(n):
    s = (1 + sqrt(24)) / 6
    return abs(round(sqrt(24 * n + 1) - s) - n) < 1e-9
def is_hexagonal(n):
    s = (1 + sqrt(3)) / 6
    return abs(round(sqrt(3 * n + 1) - s) - n) < 1e-9