def set_left_most_unset_bit(n):
    mask = n & (-n)
    mask -= 1
    return mask