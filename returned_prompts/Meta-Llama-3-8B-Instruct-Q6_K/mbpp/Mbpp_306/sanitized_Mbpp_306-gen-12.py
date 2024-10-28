def max_sum_increasing_subseq(arr, i, k, kth):
    max_sum = 0
    for j in range(i, k):
        if arr[j] < arr[kth]:
            max_sum = max(max_sum, arr[j] + max_sum_increasing_subseq(arr, j, k, kth))
    return max_sum