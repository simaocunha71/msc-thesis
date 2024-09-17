def set_left_most_unset_bit(n):
    while (n & 1) == 0:
        n >>= 1
    return n