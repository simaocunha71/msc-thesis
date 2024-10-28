def max_product(arr):
    max_prod = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_prod = max(max_prod, arr[i - 1] * arr[i])
        else:
            max_prod = max(max_prod, arr[i])
    return max_prod