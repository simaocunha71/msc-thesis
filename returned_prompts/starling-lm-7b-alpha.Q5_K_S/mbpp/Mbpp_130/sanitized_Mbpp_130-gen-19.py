def max_occurrences(nums:list)->int:
  return max(set(nums), key=(lambda x: nums.count(x)))