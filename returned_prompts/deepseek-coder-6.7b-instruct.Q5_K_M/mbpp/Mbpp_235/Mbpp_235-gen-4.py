
def even_bit_set_number(n):
    bin_n = bin(n)[2:]
    even_bits = [bin_n[i] for i in range(0, len(bin_n), 2)]
    new_bin = ''.join(even_bits)
    return int(new_bin, 2)


