def left_insertion(nums, value):
  index = 0
  while index < len(nums) and value < nums[index]:
    index += 1
  return index