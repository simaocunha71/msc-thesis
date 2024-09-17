
def set_left_most_unset_bit(n):
    count = 0
    while n:
        if n & 1 == 0:
            break
        count += 1
        n >>= 1
    return n | (1 << count)


