def sum_Of_product(n):
    import math
    sum_of_product = 0
    for i in range(n+1):
        sum_of_product += math.comb(n, i) * math.comb(n, i+1)
    return sum_of_product