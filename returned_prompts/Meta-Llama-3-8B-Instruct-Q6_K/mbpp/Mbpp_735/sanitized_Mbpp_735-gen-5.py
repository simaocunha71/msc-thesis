def toggle_middle_bits(n):
    return n ^ ((n >> 1) & ((1 << (n.bit_length() - 1)) - 1)) ^ ((1 << n.bit_length()) - 1)  # This line can be used for all python versions