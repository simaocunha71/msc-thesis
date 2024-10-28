def max_sum_increasing_subseq(arr, n, i, k):
    if k > i:
        return arr[i] + arr[k]
    else:
        return arr[i]