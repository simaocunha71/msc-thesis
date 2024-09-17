
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sub_sum = [0]*n
    sub_sum[0] = arr[0]
    prod[0] = arr[0]
    result = arr[0]
    for i in range(1, n):
        sub_sum[i] = sub_sum[i-1] + arr[i]
    for i in range(1, n):
        prod[i] = prod[i-1]*arr[i] + arr[i]
        result += prod[i]
    return result

