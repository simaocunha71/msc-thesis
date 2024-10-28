def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total = 1
    for i in range(n):
        total *= arr[i]
    for i in range(n-1, -1, -1):
        total *= arr[i]
    return total