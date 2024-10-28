def max_sum_increasing_subseq(arr, i, k, j):
    return max(arr[i] + max_sum_increasing_subseq(arr, i + 1, k, j),
               arr[j] + max_sum_increasing_subseq(arr, i, k, j - 1))