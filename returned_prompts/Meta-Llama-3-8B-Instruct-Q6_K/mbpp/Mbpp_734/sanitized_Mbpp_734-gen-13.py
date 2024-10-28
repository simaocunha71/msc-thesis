def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j+1):
                prod *= lst[k]
            total_sum += prod
    return total_sum