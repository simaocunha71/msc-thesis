def comb_sort(nums:list) -> list:
  gap = len(nums) // 2
  while gap != 0:
    for i in range(len(nums)-gap):
      if nums[i] > nums[i+gap]:
        nums[i], nums[i+gap] = nums[i+gap], nums[i]
    gap //= 2
  return nums