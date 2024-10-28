import math
def sum_Of_product(n):
    product_sum = 0
    for i in range(n):
        product_sum += math.comb(n, i) * math.comb(n, i+1)
    return product_sum