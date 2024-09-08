def even_bit_set_number(n):
    binary = bin(n)[2:]
    binary = '0b' + binary
    binary = list(binary)
    for i in range(len(binary)-1, -1, -1):
        if i % 2 == 0 and binary[i] != '1':
            binary[i] = '1'
    binary = ''.join(binary)
    return int(binary, 2)