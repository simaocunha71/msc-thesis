def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            sum += product
    return sum