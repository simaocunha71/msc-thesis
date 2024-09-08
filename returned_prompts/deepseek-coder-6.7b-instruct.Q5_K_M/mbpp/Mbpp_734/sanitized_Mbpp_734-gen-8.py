def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sub = [0]*n
    prod[0] = arr[0]
    sub[0] = 1
    for i in range(1, n):
        prod[i] = prod[i-1] + arr[i]*sub[i-1]
        sub[i] = sub[i-1] + sub[i-1]
    return sum(prod)