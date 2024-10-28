def max_sum_increasing_subseq(arr, n, k, i):
    # Initialize variables
    max_sum = -1e9
    sum = 0
    # Iterate through arr from 0 to k-1
    for j in range(0, k):
        # If j is less than i, then include it in the sum
        if j < i:
            sum += arr[j]
        # If j is greater than or equal to i, then do not include it in the sum
        else:
            break
    # Update max_sum and sum
    max_sum = max(max_sum, sum)
    # Return max_sum
    return max_sum
