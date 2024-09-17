def toggle_middle_bits(n):
    binary = bin(n)[2:]
    binary = '1' + binary[1:-1] + '1'
    return int(binary, 2)