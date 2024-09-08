def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= lst[j]
            total += prod
    return total