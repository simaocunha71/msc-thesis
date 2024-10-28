def toggle_middle_bits(n):
    if n < 1 or n > 31:
        return "Invalid input"
    binary = bin(n)[2:]
    middle_bits = binary[1:-1]
    toggled_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    return int('1' + toggled_bits + '1', 2)