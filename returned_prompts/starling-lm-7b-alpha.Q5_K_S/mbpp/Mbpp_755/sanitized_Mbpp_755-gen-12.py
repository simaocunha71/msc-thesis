def second_smallest(nums: list) -> int:
  min_num = min(nums)
  index = nums.index(min_num)
  nums.pop(index)
  return min(nums)