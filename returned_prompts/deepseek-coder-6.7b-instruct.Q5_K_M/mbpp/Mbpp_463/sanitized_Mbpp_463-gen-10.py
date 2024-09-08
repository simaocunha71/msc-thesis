def max_subarray_product(arr):
    max_end = min_end = result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_end, min_end = min_end, max_end

        max_end = max(arr[i], max_end * arr[i])
        min_end = min(arr[i], min_end * arr[i])

        result = max(result, max_end)

    return result