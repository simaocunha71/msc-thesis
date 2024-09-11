def max_sum_increasing_subseq(arr, i, k, j):
    max_sum = 0
    for x in range(i, k):
        max_sum = max(max_sum, arr[x])
    return max_sum + arr[j] if j > i else 0