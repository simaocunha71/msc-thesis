def max_sum_increasing_subseq(arr, i, k, n):
    max_sums = [0] * n

    # Initialize max_sums using prefix max sums
    max_sums[0] = arr[0]
    for i in range(1, n):
        max_sums[i] = max(max_sums[i-1], arr[i])

    # Calculate max sum of increasing subsequence including kth element
    curr_max = max_sums[i]
    curr_index = i
    while curr_index < n and arr[curr_index] < k:
        if max_sums[curr_index] > curr_max:
            curr_max = max_sums[curr_index]
            curr_index = curr_index + 1
        else:
            break

    # If kth element is found, return max sum of increasing subsequence including kth element
    if curr_index < n and arr[curr_index] == k:
        return curr_max
    # Else return the max sum of increasing subsequence till ith index
    else:
        return max_sums[i]