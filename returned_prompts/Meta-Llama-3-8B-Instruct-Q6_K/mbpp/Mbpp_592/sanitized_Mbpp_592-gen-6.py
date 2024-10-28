def sum_Of_product(n):
    sum=0
    for i in range(n+1):
        for j in range(i+1):
            sum += math.comb(n, j)
    return sum