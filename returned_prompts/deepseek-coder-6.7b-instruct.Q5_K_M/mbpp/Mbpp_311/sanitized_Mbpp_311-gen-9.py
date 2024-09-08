def set_left_most_unset_bit(n):
    if n == 0:
        return 1

    pos = 0
    while n > 0:
        if (n & 1) == 0:
            break
        n = n >> 1
        pos += 1

    return n ^ (1 << pos)