def sum_Of_Subarray_Prod(arr): 
    n = len(arr) 
    prod = [0]*n 
    subRes = [0]*n 
    subRes[0] = arr[0] 
    prod[0] = arr[0] 
    for i in range(1, n): 
        subRes[i] = ((i+1) * arr[i] + i * subRes[i-1]) 
        prod[i] = subRes[i] 
    result = 0
    for i in range(n): 
        result += prod[i] 
    return result