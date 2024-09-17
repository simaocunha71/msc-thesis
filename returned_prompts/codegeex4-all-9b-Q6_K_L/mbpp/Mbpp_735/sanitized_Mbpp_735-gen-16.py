def toggle_middle_bits(n: int) -> int:
    bit_string = bin(n)[2:]
    toggled_bit_string = ''.join('1' if bit == '0' else '0' for bit in bit_string[1:-1])
    toggled_number = int(toggled_bit_string, 2)
    return toggled_number