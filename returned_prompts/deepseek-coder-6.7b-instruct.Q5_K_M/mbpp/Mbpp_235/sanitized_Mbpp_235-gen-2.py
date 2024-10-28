def even_bit_set_number(n):
    binary = bin(n)[2:]
    binary = '0' + binary[1:] if len(binary) % 2 != 0 else binary
    binary = ''.join(['1' if i % 2 == 0 else b for i, b in enumerate(binary)])
    return int(binary, 2)