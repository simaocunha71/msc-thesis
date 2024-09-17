import math
def sum_Of_product(n):
    total = 0
    for k in range(n+1):
        total += math.comb(n, k)
    return total