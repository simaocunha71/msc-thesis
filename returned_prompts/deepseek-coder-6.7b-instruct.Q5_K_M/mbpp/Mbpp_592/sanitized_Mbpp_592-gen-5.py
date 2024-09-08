def sum_Of_product(n):
    from math import comb
    sum = 0
    for i in range(1, n):
        sum += comb(n, i) * comb(n, i+1)
    return sum