def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        temp = 1
        for j in range(i, n):
            temp *= arr[j]
            result += temp
    return result