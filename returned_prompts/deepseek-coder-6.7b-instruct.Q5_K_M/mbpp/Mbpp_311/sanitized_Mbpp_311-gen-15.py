def set_left_most_unset_bit(n):
    count = 0
    while (n):
        count += 1
        if (n & 1):
            break
        n = n >> 1
    return (n | (1 << (count - 1)))