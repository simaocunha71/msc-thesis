def toggle_middle_bits(n):
    binary = bin(n)[2:]
    middle_bits = list(binary[1:-1])
    for i in range(len(middle_bits)):
        middle_bits[i] = '1' if middle_bits[i] == '0' else '0'
    return int(binary[0] + ''.join(middle_bits) + binary[-1], 2)