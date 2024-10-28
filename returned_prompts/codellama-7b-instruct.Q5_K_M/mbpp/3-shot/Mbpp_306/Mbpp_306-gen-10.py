
def max_sum_increasing_subseq(arr, i, k, x):
    if i == k:
        return arr[i]
    elif i > k:
        return 0
    else:
        return max(arr[i] + max_sum_increasing_subseq(arr, i+1, k, x),
                   max_sum_increasing_subseq(arr, i+1, k, x))


