def set_left_most_unset_bit(n):
    pos = 0
    while n & (1 << pos):
        pos += 1
    return n | (1 << pos)