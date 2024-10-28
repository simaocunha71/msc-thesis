def max_sub_array_sum(nums: list, k: int) -> int:
    if len(nums) < k:
        return sum(nums)
    max_sum = sum(nums[:k])
    current_sum = max_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum

