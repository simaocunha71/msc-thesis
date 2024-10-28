def max_sum_increasing_subseq(arr, i, k):
    """
    This function takes in an array of integers, an index i, and a value k.
    It returns the maximum sum of an increasing subsequence from the prefix until index i,
    including the kth element which is after i.
    """
    max_sum = 0
    current_sum = 0
    for j in range(i+1, k+1):
        if arr[j] > arr[i]:
            current_sum += arr[j]
        else:
            current_sum = arr[j]
        max_sum = max(max_sum, current_sum)
    return max_sum