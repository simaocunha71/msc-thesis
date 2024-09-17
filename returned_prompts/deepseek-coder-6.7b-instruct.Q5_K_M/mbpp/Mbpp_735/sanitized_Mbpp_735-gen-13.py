def toggle_middle_bits(n):
    binary = bin(n)[2:]
    binary = list(binary)
    for i in range(1, len(binary)-1):
        if binary[i] == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'
    return int(''.join(binary), 2)