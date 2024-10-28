def max_subarray_product(arr):
    max_product = arr[0]
    for i in range(1, len(arr)):
        max_product = max(max_product, max_product * arr[i], arr[i])
    return max_product