def sum_Of_product(n):
    sum_of_product = 0
    for i in range(1, n+1):
        product = 1
        for j in range(i):
            product *= (n-j)
        sum_of_product += product
    return sum_of_product