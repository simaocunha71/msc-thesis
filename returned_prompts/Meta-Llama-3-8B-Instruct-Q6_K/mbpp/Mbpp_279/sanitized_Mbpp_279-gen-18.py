def is_num_decagonal(n):
    if n < 1:
        return 0
    else:
        return n * (3 * n - 1)