"""
def max_sum_increasing_subseq(arr, k, i, j):
    if i == j:
        return arr[i]
    else:
        return max(arr[i] + max_sum_increasing_subseq(arr, k, i+1, j),
                   max_sum_increasing_subseq(arr, k, i+1, j))

def max_sum_increasing_subseq(arr, k, i):
    return max_sum_increasing_subseq(arr, k, 0, i)
"""
