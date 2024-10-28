def sum_Of_product(n):
    sum_of_product = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            sum_of_product += 1
            if i > 1:
                sum_of_product *= i
            if j > 1:
                sum_of_product /= j
    return sum_of_product