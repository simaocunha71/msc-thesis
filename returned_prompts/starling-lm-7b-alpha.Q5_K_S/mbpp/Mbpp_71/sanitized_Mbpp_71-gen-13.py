def comb_sort(nums: list) -> list:
  gap = len(nums)
  swapped = True
  while gap != 0 and swapped:
    gap = max(1, int(gap/1.3))
    swapped = False
    for i in range(len(nums)-gap):
      if nums[i] > nums[i+gap]:
        nums[i], nums[i+gap] = nums[i+gap], nums[i]
        swapped = True
  return nums