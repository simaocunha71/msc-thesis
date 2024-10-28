def sum_Of_product(n):
    result = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            result += math.comb(n, i) * math.comb(n, j)
    return result