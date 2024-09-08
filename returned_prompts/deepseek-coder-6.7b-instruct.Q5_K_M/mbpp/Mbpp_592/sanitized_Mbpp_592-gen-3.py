def sum_Of_product(n):
    import math
    sum_val = 0
    for i in range(n):
        sum_val += math.comb(n, i) * math.comb(n, i + 1)
    return sum_val