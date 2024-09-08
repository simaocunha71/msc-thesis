def max_sum_increasing_subseq(arr, k, i, j):
    if i >= j or k <= i:
        return 0
    max_sum = 0
    for m in range(i+1, k):
        if arr[m] > arr[i]:
            max_sum = max(max_sum, max_sum_increasing_subseq(arr, k, m, j))
    return max_sum + arr[i]