from math import comb
from math import factorial
from math import sqrt
from math import log
def count_binary_seq(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    sum_first_n = 2**n - 1
    sum_last_n = 2**n - 1

    return comb(2*n, n) * 2**(-n)