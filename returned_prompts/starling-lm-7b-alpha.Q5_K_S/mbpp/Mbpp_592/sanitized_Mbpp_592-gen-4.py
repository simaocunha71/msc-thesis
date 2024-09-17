def sum_Of_product(n):
    if n < 0:
        return None
    sum_ = 0
    for i in range(2, n + 1):
        for j in range(i + 1):
            sum_ += pow(j, 2)
    return sum_