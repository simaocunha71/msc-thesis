def even_bit_set_number(n):
    binary = bin(n)[2:]
    binary = list(binary)
    for i in range(0, len(binary), 2):
        binary[i] = '1'
    return int(''.join(binary), 2)