def toggle_middle_bits(n):
    binary_str = bin(n)[2:]
    toggle_str = binary_str[0] + ''.join('1' if bit == '0' else '0' for bit in binary_str[1:-1]) + binary_str[-1]
    return int(toggle_str, 2)