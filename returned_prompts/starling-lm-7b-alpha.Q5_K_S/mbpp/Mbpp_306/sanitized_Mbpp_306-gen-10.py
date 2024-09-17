def max_sum_increasing_subseq(arr, i, k, n):
    if k > n:
        return -float('inf')
    if k == n:
        return arr[k-1]
    max_sum_until_i = [0]*i
    max_sum_until_i[0] = arr[0]
    for j in range(1, i):
        max_sum_until_i[j] = max(max_sum_until_i[j-1], arr[j])
    max_sum_from_k = arr[k-1]
    for j in range(k-2, -1, -1):
        if arr[j] < arr[j+1]:
            max_sum_from_k += arr[j]
        else:
            max_sum_from_k = arr[j]
    return max(max_sum_until_i[i-1], max_sum_from_k)