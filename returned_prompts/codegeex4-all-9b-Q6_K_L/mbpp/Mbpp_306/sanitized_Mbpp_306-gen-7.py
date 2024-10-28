def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize a list to store the maximum sum of increasing subsequence ending at each index
    max_sum = [0] * n

    # Initialize the maximum sum of increasing subsequence ending at index i
    max_sum[i] = arr[i]

    # Iterate over the array starting from index i+1 to k
    for j in range(i+1, k+1):
        # Initialize the maximum sum of increasing subsequence ending at index j
        current_sum = arr[j]

        # Iterate over the array from index i to j-1
        for l in range(i, j):
            # Check if the current element is greater than the previous element
            if arr[l] < arr[j]:
                # Update the maximum sum of increasing subsequence ending at index j
                current_sum = max(current_sum, max_sum[l] + arr[j])

        # Update the maximum sum of increasing subsequence ending at index j
        max_sum[j] = current_sum

    # Return the maximum sum of increasing subsequence ending at index k
    return max_sum[k]