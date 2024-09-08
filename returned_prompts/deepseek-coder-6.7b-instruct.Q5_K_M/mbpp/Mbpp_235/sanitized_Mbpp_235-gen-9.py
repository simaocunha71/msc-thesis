def even_bit_set_number(n):
    binary = bin(n)[2:] # remove '0b' from the start
    even_bits = [binary[i] for i in range(0, len(binary), 2)]
    even_bits = ''.join(even_bits)
    return int(even_bits, 2)