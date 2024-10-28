def pancake_sort(nums: list) -> list:
  for i in range(len(nums)):
    max_index = nums.index(max(nums[i:]))
    if max_index != i:
      nums[i:max_index+1] = reversed(nums[i:max_index+1])
      nums[:i+1] = reversed(nums[:i+1])
  return nums

