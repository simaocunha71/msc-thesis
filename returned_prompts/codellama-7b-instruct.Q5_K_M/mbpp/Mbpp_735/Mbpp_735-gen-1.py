def toggle_middle_bits(n):
    mask = 0x33333333
    return (n | mask) & ~mask


