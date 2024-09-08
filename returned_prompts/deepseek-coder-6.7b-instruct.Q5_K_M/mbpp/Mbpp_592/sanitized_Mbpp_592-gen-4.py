def sum_Of_product(n):
    import math
    sum = 0
    for i in range(1, n):
        sum += math.comb(n, i) * math.comb(n, i+1)
    return sum