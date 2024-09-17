def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    result = 0
    for i in range(2**n):
        curr = 0
        for j in range(n):
            if (i & (1 << j)):
                curr += lst[j]
        result += curr
    return result