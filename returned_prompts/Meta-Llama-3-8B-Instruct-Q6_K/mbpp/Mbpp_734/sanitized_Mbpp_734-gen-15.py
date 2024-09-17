def sum_Of_Subarray_Prod(lst):
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    total_sum = prod
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            subarray = lst[i:j]
            prod = 1
            for num in subarray:
                prod *= num
            total_sum += prod
    return total_sum