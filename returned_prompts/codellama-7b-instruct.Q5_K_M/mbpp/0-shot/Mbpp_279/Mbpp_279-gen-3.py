def is_num_decagonal(n):
    return n * (n + 1) == (8 * n + 1) ** 2

def nth_decagonal(n):
    return int(((8 * n + 1) ** 2 + 1) ** 0.5 / 2)
