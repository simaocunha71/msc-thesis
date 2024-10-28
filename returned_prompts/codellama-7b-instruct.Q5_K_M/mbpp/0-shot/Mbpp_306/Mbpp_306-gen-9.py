"""
def max_sum_increasing_subseq(arr, i, k, j):
    if i == j:
        return arr[i]
    if k == i:
        return max(arr[i], arr[i] + max_sum_increasing_subseq(arr, i + 1, k, j))
    if k == j:
        return max(arr[j], max_sum_increasing_subseq(arr, i, k, j - 1))
    return max(arr[k], arr[i] + max_sum_increasing_subseq(arr, i + 1, k, j), arr[j] + max_sum_increasing_subseq(arr, i, k - 1, j - 1))
"""
