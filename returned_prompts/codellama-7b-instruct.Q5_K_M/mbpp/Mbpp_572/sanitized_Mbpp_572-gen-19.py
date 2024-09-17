def two_unique_nums(nums):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] == nums[j]:
        nums.remove(nums[j])
  return nums