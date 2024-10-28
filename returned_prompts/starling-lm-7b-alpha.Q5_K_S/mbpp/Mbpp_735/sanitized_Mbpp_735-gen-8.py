def toggle_middle_bits(n):
    # Shift all bits to the right, except for the last bit
    n = (n >> 1) | (n & 1) << 1
    # Shift the last bit to the end and toggle all other bits
    return (n ^ (n >> 1))