
def max_sum_increasing_subseq(arr, i, k, j):
    return max(arr[i] + max_sum_increasing_subseq(arr, i + 1, k, j),
               arr[j] + max_sum_increasing_subseq(arr, i, k, j - 1))

def max_sum_increasing_subseq(arr, i, k):
    return max_sum_increasing_subseq(arr, i, k, len(arr) - 1)

max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6)

