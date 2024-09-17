def max_sub_array_sum(nums: list, size: int) -> int:
  max_sum = 0
  for i in range(len(nums) - size + 1):
    max_sum = max(max_sum, sum(nums[i:i + size]))
  return max_sum