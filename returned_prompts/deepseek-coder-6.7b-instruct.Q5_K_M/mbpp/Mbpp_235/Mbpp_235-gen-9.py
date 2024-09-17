
def even_bit_set_number(n):
    binary = bin(n)[2:]
    for i in range(0, len(binary), 2):
        n = n | (1 << int(binary[i:i+2], 2))
    return n


