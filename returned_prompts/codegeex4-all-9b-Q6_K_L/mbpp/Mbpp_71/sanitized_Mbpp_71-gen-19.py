def comb_sort(nums: list) -> list:
  gap = len(nums)
  while gap > 1:
    gap = (gap * 10)//13
    for i in range(len(nums)-gap):
      if nums[i] > nums[i+gap]:
        nums[i], nums[i+gap] = nums[i+gap], nums[i]
  return nums