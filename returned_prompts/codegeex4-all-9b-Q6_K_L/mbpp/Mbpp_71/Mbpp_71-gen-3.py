def comb_sort(nums: list) -> list:
  gap = len(nums)
  shrink = 1.3
  while gap > 1:
    gap = int(gap/shrink)
    for i in range(len(nums)-gap):
      if nums[i] > nums[i+gap]:
        nums[i], nums[i+gap] = nums[i+gap], nums[i]
  return nums

