def is_num_decagonal(n):
    if n < 3:
        return False
    return ((n - 3) * 2) % 3 == 0