import math
def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return math.comb(2*n, n) // (n + 1)  # // is the integer division operator in Python