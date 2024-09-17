from math import comb
def sum_Of_product(n):
    if n < 1:
        return 0
    else:
        return sum(comb(2*i, i) for i in range(n+1))