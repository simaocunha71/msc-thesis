def is_num_decagonal(n):
    return int(n * (n - 1) * (3*n - 1) / 2) if n > 0 else 0