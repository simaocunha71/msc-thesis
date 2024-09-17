def find_first_occurrence(nums, target):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
  return -1