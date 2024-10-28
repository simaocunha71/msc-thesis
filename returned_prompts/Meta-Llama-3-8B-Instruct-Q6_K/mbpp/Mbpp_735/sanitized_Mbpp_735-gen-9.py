def toggle_middle_bits(n):
    return ((n & 1) | ((n >> 1) & 0x55555555)) << 1 | n & 1