def max_product(arr):
    if not arr:
        return 0

    max_product = min_product = result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            max_product, min_product, result = min_product, max_product, max(min_product, result)
        max_product *= arr[i]
        min_product = min(min_product, arr[i])

    return result