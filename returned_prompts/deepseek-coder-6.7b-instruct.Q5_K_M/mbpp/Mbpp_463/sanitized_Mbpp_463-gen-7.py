def max_subarray_product(arr):
    n = len(arr)
    max_end_here = arr[0]
    min_end_here = arr[0]
    max_so_far = arr[0]
    for i in range(1, n):
        max_end_here = max(arr[i], max_end_here * arr[i], min_end_here * arr[i])
        min_end_here = min(arr[i], max_end_here * arr[i], min_end_here * arr[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far