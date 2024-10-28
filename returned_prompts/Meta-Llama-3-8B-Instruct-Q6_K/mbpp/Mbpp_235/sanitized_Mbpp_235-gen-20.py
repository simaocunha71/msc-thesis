def even_bit_set_number(n):
    result = 0
    while n > 0:
        if n & 1:
            result = result | 2
        n = n >> 1
    return result