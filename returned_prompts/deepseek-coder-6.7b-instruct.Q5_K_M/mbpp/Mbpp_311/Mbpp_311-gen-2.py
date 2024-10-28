
def set_left_most_unset_bit(n):
    return n | (1 << (bin(n)[2:].index('0') if '0' in bin(n)[2:] else len(bin(n)[2:])))


