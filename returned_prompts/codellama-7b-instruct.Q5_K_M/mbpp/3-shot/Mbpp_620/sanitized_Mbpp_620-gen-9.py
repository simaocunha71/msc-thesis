def largest_subset(nums: list) -> int:
  nums = sorted(nums)
  max_subset = 0
  for i, num in enumerate(nums):
    if num % 2 == 0:
      max_subset = max(max_subset, i+1)
    else:
      for j in range(i, 0, -1):
        if nums[j] % nums[i] == 0:
          max_subset = max(max_subset, j+1)
          break
  return max_subset