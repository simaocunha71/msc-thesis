def max_product(arr):
    n = len(arr)
    prod = [0]*n
    prod[0] = arr[0]

    for i in range(1, n):
        prod[i] = max(arr[i], prod[i-1]*arr[i])

    result = prod[0]
    for i in range(1, n):
        result = max(result, prod[i])

    return result