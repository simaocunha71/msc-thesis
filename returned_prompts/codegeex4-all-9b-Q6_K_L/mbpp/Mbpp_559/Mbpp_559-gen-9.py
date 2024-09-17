def max_sub_array_sum(nums: list, n: int) -> int:
    max_sum = float('-inf')
    for i in range(n, len(nums)+1):
        sub_array = nums[i-n:i]
        current_sum = sum(sub_array)
        max_sum = max(max_sum, current_sum)
    return max_sum

