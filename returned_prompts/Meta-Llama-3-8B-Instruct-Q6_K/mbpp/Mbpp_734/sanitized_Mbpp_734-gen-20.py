def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            res += math.prod(lst[i:j+1])
    return res