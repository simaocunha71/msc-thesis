def max_sub_array_sum(arr: list, k: int) -> int:
    max_sum = float('-inf')
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k:
            window_sum -= arr[i - k]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
    return max_sum