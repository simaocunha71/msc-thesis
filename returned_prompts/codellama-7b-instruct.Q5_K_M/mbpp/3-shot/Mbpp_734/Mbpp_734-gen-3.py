
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] * arr[1]
    if n == 3:
        return arr[0] * arr[1] * arr[2] + arr[0] * arr[2] * arr[1] + arr[1] * arr[0] * arr[2]

    result = 0
    for i in range(n):
        result += arr[i] * (sum_Of_Subarray_Prod(arr[i+1:]) + sum_Of_Subarray_Prod(arr[:i]) + sum_Of_Subarray_Prod(arr[i+1:]))
    return result


