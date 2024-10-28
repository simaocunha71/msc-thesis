def toggle_middle_bits(n):
    binary = bin(n)[2:]
    toggled_binary = ''.join('1' if x == '0' else '0' for x in binary[1:-1])
    toggled_number = int(toggled_binary, 2)
    return toggled_number

