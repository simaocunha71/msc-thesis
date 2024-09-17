def even_bit_set_number(n):
    result = 0
    i = 0
    while n > 0:
        if (n & 1) == 0:
            result |= 1 << i
        n >>= 1
        i += 1
    return result