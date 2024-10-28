def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    total = sum(lst)
    res = 0
    for i in range(n):
        res += lst[i] * (total - lst[i])
    return res