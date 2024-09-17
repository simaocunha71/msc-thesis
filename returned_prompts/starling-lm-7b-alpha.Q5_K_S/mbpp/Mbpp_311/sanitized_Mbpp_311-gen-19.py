def set_left_most_unset_bit(n):
    i = 0
    while (n & 1) == 0:
        i += 1
        n >>= 1
    return n | (1 << i)