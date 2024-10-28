def max_sum_increasing_subseq(arr, i, k, n):
    if i == n or k == i:
        return 0
    return max(arr[i] + max_sum_increasing_subseq(arr, i + 1, k, n), max_sum_increasing_subseq(arr, i + 1, k, n))