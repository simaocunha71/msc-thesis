def toggle_middle_bits(n):
    # create a mask to toggle all bits except the first and the last
    mask = (2 << (n.bit_length() - 2)) - 1
    # toggle the bits
    return n ^ mask