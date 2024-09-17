
def even_bit_set_number(n):
    while n & 1 == 0:
        n >>= 1
    return n << 1


