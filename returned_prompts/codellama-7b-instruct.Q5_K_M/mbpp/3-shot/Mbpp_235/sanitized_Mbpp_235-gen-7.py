def even_bit_set_number(n):
    return n | (n & -n)