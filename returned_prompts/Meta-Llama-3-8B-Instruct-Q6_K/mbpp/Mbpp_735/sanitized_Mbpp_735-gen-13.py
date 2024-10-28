def toggle_middle_bits(n):
    if n < 0:
        return -toggle_middle_bits(-n)
    if n < 2:
        return n
    mask = (1 << (n.bit_length() - 1)) - 1
    return n ^ mask