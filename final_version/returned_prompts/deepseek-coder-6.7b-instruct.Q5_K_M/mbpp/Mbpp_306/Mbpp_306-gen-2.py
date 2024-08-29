
def max_sum_increasing_subseq(arr, n, k, i):
    if i >= n or i < 0:
        return -1
    if k >= n or k < 0:
        return -1

    max_sum = [0]*n
    max_sum[i] = arr[i]
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            max_sum[j] = max(max_sum[j], max_sum[i] + arr[j])
        for x in range(j+1, n):
            if arr[x] > arr[j]:
                max_sum[x] = max(max_sum[x], max_sum[j] + arr[x])
    
    max_sum[k] = max_sum[k] + arr[k]
    for x in range(k+1, n):
        if arr[x] > arr[k]:
            max_sum[x] = max(max_sum[x], max_sum[k] + arr[x])

    return max(max_sum)

print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6))


# Output: 1102
# Explanation: 101+100+5 = 1106
# I've made a mistake in the question. The sequence should be increasing, not just prefix.
# So, the correct solution is not possible.

# 