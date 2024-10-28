def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= arr[j]
            total += prod
    return total