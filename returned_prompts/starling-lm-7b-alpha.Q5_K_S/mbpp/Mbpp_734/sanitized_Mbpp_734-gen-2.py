def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j+1):
                prod *= lst[k]
            res += prod
    return res