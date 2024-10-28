def max_sum_increasing_subseq(arr, i, k, prefix_sum):
    if i == 0:
        return prefix_sum
    max_sum = prefix_sum
    for j in range(i):
        if arr[j] < arr[i]:
            max_sum = max(max_sum, max_sum_increasing_subseq(arr, j, k, prefix_sum + arr[j]))
    if k > i:
        max_sum = max(max_sum, max_sum_increasing_subseq(arr, i + 1, k, prefix_sum + arr[i]))
    return max_sum