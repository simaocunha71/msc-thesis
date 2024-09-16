def set_left_most_unset_bit(n):
    i = 1
    while n & i != 0:
        i <<= 1
    return n | i