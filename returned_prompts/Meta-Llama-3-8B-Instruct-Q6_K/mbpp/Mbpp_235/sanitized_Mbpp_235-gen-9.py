def even_bit_set_number(n):
    return n | ((n >> 1) & 0xAAAAAAAA)  # Assuming 32-bit integer