def max_sub_array_sum(arr, k):
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum = max(curr_sum + arr[i], arr[i])
        if curr_sum == k:
            return k
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum