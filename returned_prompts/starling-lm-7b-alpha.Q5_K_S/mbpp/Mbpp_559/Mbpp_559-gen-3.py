
def max_sub_array_sum(nums: list, k: int) -> int:
    window_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k:
            window_sum -= nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum


