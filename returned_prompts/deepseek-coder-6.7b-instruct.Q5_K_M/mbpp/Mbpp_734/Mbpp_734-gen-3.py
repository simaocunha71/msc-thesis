
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    prod = [0]*n
    subarray_sum = [0]*n
    prod[0] = lst[0]
    subarray_sum[0] = lst[0]
    for i in range(1, n):
        prod[i] = max(lst[i], prod[i-1]*lst[i])
        subarray_sum[i] = prod[i] + subarray_sum[i-1]
    return subarray_sum[-1]


