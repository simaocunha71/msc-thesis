def toggle_middle_bits(n: int) -> int:
    first_bit, last_bit = n&1, n&2**(n.bit_length()-1)
    return (n^2**(n.bit_length()-1)) | (first_bit<<1) | last_bit