
def max_subarray_product(arr):
    max_product = arr[0]
    min_product = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]

    for i in range(1, len(arr)):
        max_product = max(arr[i], max_product * arr[i], min_product * arr[i])
        min_product = min(arr[i], max_product * arr[i], min_product * arr[i])
        max_so_far = max(max_so_far, max_product)
        min_so_far = min(min_so_far, min_product)

    return max_so_far


