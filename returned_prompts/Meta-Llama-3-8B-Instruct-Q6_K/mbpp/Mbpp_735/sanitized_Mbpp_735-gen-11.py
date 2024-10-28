def toggle_middle_bits(n):
    if n < 0:
        n = ~n + 1
    bin_n = bin(n)[2:]
    first_bit, *middle_bits, last_bit = bin_n
    middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    return int('1' + middle_bits + last_bit, 2)