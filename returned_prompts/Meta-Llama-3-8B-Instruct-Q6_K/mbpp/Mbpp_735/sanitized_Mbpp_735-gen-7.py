def toggle_middle_bits(n):
    return (n & 1) | ((n >> 1) & ~((~0 << (n.bit_length() - 1)) >> 1)) << 1 | ((n & 0) | ((n >> 1) & 1) << (n.bit_length() - 1))  # noqa: E501
    # or 
    # n ^ ((n >> 1) ^ ((~0 << (n.bit_length() - 1)) >> 1)) << 1