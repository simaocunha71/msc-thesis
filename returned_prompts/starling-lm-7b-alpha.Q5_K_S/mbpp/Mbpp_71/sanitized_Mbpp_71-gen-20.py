def comb_sort(nums:list):
  gap = len(nums) // 2
  swapped = True
  while gap != 0 and swapped:
    gap = gap // 2
    swapped = False
    for i in range(len(nums) - gap):
      if nums[i] > nums[i + gap]:
        nums[i], nums[i + gap] = nums[i + gap], nums[i]
        swapped = True
  return nums