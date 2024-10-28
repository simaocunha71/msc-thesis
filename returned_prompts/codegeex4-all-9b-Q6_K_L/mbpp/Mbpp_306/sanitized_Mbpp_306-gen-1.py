def max_sum_increasing_subseq(arr, k, i, j):
    max_sum = 0

    # Iterate over the elements from i+1 to k
    for l in range(i+1, k):
        # If the current element is greater than previous element
        if arr[l] > arr[l-1]:
            # Calculate the sum of the subsequence from i to l
            subseq_sum = sum(arr[i:l+1])

            # If the sum is greater than max_sum, update max_sum
            if subseq_sum > max_sum:
                max_sum = subseq_sum

    # Return the maximum sum of the increasing subsequence
    return max_sum