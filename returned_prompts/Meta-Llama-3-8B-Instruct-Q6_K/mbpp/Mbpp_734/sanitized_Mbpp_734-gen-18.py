def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total_sum = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= lst[j]
            total_sum += prod
    return total_sum