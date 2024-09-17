
def toggle_middle_bits(n):
    flip_bit = ~1 << 1
    flip_bit2 = ~1 << (n.bit_length() - 1)
    return n ^ flip_bit ^ flip_bit2


