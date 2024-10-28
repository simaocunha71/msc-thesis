def toggle_middle_bits(n):
    first_bit, last_bit = n&1, n&(1<<(n.bit_length()-1))
    return (first_bit<<(n.bit_length()-1)) | (last_bit>>1) | (1<<(n.bit_length()-2)) | (n^last_bit)