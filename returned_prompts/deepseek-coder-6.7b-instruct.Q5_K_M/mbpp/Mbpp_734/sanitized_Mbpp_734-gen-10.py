def sum_Of_Subarray_Prod(l):
    n = len(l)
    sum_ = 0
    prod = 1
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= l[j]
            sum_ += prod
    return sum_