def max_sub_array_sum(nums: list, k: int) -> int:
    return sum(nums[i:i+k] for i in range(len(nums) - k + 1))