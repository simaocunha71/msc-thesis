def max_sum_increasing_subseq(arr, k, i, j):
    if i > j or k > len(arr):
        return 0
    if i == j:
        return arr[i] if arr[i] <= arr[k] else 0
    if j == k:
        return arr[j] if arr[j] > arr[k] else 0
    return max(arr[i] + max_sum_increasing_subseq(arr, k, i+1, j), arr[j] + max_sum_increasing_subseq(arr, k, i, j-1))