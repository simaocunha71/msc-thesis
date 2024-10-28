"""
def max_sub_array_sum_repeated(arr, k, n):
    max_sum = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if j - i + 1 > k:
                curr_sum -= arr[j - k]
            max_sum = max(max_sum, curr_sum)
    return max_sum
"""
