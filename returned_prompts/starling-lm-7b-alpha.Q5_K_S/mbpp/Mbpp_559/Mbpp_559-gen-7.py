
def max_sub_array_sum(nums: list, k: int) -> int:
    if k == 0:
        return 0
    window_start = 0
    window_sum = 0
    max_window_sum = float('-inf')

    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        while window_sum > k:
            window_sum -= nums[window_start]
            window_start += 1
        max_window_sum = max(max_window_sum, window_sum)

    return max_window_sum


