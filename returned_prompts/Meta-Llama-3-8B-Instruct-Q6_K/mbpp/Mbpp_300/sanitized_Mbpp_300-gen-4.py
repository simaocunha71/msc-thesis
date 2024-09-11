from math import comb
import math
def count_binary_seq(n):
    return comb(2**n, n) + comb(2**n, n-1) - 2*comb(2**n, n-1) + 1