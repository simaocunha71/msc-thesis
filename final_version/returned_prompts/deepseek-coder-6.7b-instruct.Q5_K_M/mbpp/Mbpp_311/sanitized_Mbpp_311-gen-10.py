def set_left_most_unset_bit(n):
    if n & 1 == 0:
        return n | 1
    else:
        return n