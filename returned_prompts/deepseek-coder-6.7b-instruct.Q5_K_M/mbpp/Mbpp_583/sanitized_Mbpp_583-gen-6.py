import math
def catalan_number(n):
    return math.comb(2*n, n) // (n+1)