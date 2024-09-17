
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    i = 0
    while n > 0:
        i += 1
        n >>= 1
    return 1 << i


