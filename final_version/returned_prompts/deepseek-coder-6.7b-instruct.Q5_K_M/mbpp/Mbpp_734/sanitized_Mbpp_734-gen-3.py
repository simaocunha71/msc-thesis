def sum_Of_Subarray_Prod(lst):
    sum_prod = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            prod = 1
            for k in sublist:
                prod *= k
            sum_prod += prod
    return sum_prod