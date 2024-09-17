def max_occurrences(nums: list) -> list:
  return max(set(nums), key = nums.count)