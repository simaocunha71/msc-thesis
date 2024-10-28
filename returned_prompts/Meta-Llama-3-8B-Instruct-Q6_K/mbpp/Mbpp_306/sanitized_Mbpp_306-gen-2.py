def max_sum_increasing_subseq(arr, i, k, n):
    max_sum = 0
    for j in range(i, k):
        if arr[j] > arr[i]:
            max_sum += arr[j]
    return max_sum + arr[k]