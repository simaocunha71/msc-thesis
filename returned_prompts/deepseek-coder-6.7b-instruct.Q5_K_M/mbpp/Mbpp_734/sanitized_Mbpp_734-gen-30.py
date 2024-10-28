def sum_Of_Subarray_Prod(arr): 
    n = len(arr) 
    prod = [0]*n 
    sub_sum = [0]*n 
    prod[0] = arr[0] 
    sub_sum[0] = arr[0] 
    res = arr[0] 
    for i in range(1, n): 
        prod[i] = max(arr[i], prod[i - 1] * arr[i]) 
        sub_sum[i] = max(prod[i], sub_sum[i - 1] + arr[i]) 
        res += sub_sum[i] 
    return res