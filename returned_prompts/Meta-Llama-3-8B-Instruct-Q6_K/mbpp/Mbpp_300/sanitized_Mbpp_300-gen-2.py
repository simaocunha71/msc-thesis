from math import comb
def count_binary_seq(n):
    return comb(2**n, n) * 2