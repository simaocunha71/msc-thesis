def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total = 0
    for i in range(1 << n):
        product = 1
        for j in range(n):
            if (i & (1 << j)):
                product *= lst[j]
        total += product
    return total