def set_left_most_unset_bit(n):
    bin_n = bin(n)[2:]
    for i in range(len(bin_n)):
        if bin_n[i] == '0':
            return n | 2 ** (len(bin_n) - i - 1)
    return n