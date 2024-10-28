def max_occurrences(nums: list) -> int:
  return max(set(nums), key = nums.count)