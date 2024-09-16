
def max_sum_increasing_subseq(arr, i, k, n):
    if i >= n or k > n or i < 0 or k < 0:
        return 0
    if k == i + 1:
        return arr[i]
    if k == i:
        return max(arr[i], arr[k])
    return max(arr[i] + max_sum_increasing_subseq(arr, i + 1, k - 1, n), max_sum_increasing_subseq(arr, i + 1, k, n))
