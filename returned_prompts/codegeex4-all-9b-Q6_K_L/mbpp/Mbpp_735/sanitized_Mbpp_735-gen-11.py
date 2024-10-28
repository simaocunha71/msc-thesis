def toggle_middle_bits(n):
    return n ^ (n >> 1) ^ (n << 1)