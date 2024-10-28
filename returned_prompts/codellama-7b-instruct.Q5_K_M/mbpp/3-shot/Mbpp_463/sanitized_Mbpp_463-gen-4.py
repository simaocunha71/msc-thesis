def max_subarray_product(arr: list) -> int:
    max_product = arr[0]
    current_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max * arr[i], current_max - arr[i])
        max_product = max(max_product, current_max)
    return max_product