
def set_left_most_unset_bit(n):
    for i in range(0, 32):
        if ((n >> i) & 1) == 0:
            return n | (1 << i)
    return -1


