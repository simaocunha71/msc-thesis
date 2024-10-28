def max_subarray_product(arr):
    # Initialize variables
    max_product = arr[0]
    max_ending_here = arr[0]
    max_so_far = arr[0]
    min_ending_here = arr[0]
    min_so_far = arr[0]

    # Traverse the array
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here * arr[i], min_ending_here * arr[i])
        max_so_far = max(max_so_far, max_ending_here)
        min_ending_here = min(arr[i], max_ending_here * arr[i], min_ending_here * arr[i])
        min_so_far = min(min_so_far, min_ending_here)

    return max_so_far