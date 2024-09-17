
def largest_subset(nums: list) -> int:
  nums.sort()
  i = 0
  j = 1
  subset_len = 0
  while j < len(nums):
    if nums[j] % nums[i] == 0:
      j += 1
      subset_len += 1
    else:
      i += 1
  return subset_len


