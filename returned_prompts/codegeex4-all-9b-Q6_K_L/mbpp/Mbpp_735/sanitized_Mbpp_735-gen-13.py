def toggle_middle_bits(n):
    binary = bin(n)[2:]
    middle_bits = binary[1:-1]
    toggled_middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    result = int(toggled_middle_bits, 2) << len(binary) - 2
    return result + int(binary[:1] + binary[-1:], 2)