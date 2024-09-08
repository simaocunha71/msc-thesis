def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_total = 0
    for i in range(n):
        prod[i] = arr[i]*(i+1)
        sum_total += prod[i]
    return sum_total