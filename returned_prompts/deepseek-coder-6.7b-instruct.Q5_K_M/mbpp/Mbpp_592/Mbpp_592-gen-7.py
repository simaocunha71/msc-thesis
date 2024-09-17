
import math
def sum_Of_product(n):
    sum = 0
    for i in range(1, n):
        sum += math.comb(n, i) * math.comb(n, i+1)
    return sum


