def max_sum_increasing_subseq(arr, k, i, j):
    # Initialize the maximum sum to 0
    max_sum = 0

    # Iterate over the subarray from i to j
    for x in range(i, j+1):
        # Iterate over the subarray from x to k
        for y in range(x, k+1):
            # If the subsequence is increasing, update the maximum sum
            if arr[y] > arr[x]:
                max_sum = max(max_sum, arr[y])

    return max_sum