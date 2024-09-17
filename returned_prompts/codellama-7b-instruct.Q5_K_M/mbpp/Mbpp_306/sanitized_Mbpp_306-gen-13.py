def max_sum_increasing_subseq(arr, n, k, i):
    if i == n or k == n:
        return 0
    else:
        return max(arr[i] + max_sum_increasing_subseq(arr, n, k + 1, i + 1),
                   max_sum_increasing_subseq(arr, n, k, i + 1))