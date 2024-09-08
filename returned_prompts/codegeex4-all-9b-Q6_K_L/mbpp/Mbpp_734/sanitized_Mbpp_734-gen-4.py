def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subarray = lst[i:j+1]
            prod = 1
            for num in subarray:
                prod *= num
            res += prod
    return res