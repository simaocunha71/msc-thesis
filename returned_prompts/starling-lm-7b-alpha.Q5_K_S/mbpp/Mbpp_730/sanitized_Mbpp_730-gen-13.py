def consecutive_duplicates(nums: list) -> list:
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
      nums.pop(i+1)
  return nums