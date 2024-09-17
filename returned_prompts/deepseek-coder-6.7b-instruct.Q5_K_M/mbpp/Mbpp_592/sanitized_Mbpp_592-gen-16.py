from math import comb
def sum_Of_product(n):
    sum_val = 0
    for i in range(1, n):
        sum_val += comb(n, i) * comb(n, i+1)
    return sum_val