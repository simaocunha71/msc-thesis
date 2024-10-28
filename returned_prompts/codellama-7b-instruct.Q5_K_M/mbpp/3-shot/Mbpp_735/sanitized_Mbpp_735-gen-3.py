def toggle_middle_bits(n):
    first_bit, last_bit = n&1, n&(1<<(n.bit_length()-1))
    return (n >> 1) | (1 - last_bit << (n.bit_length()-1)) | first_bit