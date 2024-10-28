def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0]*arr[1]
    return arr[0]*sum_Of_Subarray_Prod(arr[1:]) + arr[n-1]*sum_Of_Subarray_Prod(arr[:n-1])