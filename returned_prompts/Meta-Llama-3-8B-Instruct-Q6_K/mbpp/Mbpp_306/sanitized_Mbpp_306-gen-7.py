def max_sum_increasing_subseq(arr, i, k, max_val):
    max_sum = 0
    for j in range(i, k):
        if arr[j] <= max_val:
            max_sum += arr[j]
            max_val = arr[j]
    return max_sum + max_val