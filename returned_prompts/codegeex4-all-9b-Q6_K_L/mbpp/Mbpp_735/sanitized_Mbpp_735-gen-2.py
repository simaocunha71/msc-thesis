def toggle_middle_bits(n):
    # Create a mask with all bits set to 1 except the first and last bit
    mask = (1 << (n.bit_length() - 1)) | 1
    # Toggle the middle bits using bitwise XOR
    return n ^ mask