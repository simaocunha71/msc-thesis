def set_left_most_unset_bit(n):
    if n & 1 == 0:
        return n | 1
    else:
        count = 0
        while n:
            if n & 1 == 0:
                return n | (1 << count)
            count += 1
            n >>= 1
    return n