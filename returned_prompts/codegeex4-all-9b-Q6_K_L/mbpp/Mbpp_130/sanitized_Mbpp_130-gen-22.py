def max_occurrences(nums: list) -> int:
  max_num = max(set(nums), key=nums.count)
  return max_num