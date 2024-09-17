
def even_bit_set_number(n):
    bin_n = bin(n)[2:]
    new_bin = ''.join(['1' if i%2 == 0 else bin_n[i] for i in range(len(bin_n))])
    return int(new_bin, 2)


