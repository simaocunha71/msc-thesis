def is_octagonal(n):
    x = (1 + 2 * math.sqrt(3)) ** (n + 1) - 1
    return int(round(x / 2))