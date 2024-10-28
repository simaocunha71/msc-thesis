import math
def count_binary_seq(n):
    return math.comb(2*n, n) * 2**n