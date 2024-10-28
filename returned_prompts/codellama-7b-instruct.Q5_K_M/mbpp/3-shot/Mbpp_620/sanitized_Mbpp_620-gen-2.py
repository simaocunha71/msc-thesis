def largest_subset(nums: list) -> int:
  max_subset = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if nums[j] % nums[i] == 0:
        max_subset += 1
  return max_subset