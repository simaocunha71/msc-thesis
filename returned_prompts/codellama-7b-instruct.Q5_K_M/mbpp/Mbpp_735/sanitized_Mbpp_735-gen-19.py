def toggle_middle_bits(n):
    first_bit = n & 1
    last_bit = n & 1 << (n.bit_length() - 1)
    other_bits = n ^ (n & (n - 1))
    return first_bit | last_bit | other_bits