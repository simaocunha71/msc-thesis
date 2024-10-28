def pancake_sort(nums: list) -> list:
  for i in range(len(nums)-1, 0, -1):
    if nums[i] == i:
      continue
    else:
      nums.insert(i, nums.pop(i))
  return nums