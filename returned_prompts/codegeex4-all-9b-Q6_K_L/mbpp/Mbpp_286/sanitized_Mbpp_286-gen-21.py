def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
    prefix_sum = [0] * (n+1)
    curr_sum = 0
    max_sum = float('-inf')
    for i in range(n):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum - prefix_sum[i])
        if curr_sum < 0:
            curr_sum = 0
        prefix_sum[i+1] = curr_sum
    for i in range(1, k):
        max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-1])
    return max_sum