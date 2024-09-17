def sum_Of_product(n):
    sum = 0
    for i in range(n+1):
        for j in range(i, n+1):
            sum += 2**(j-i)
    return sum