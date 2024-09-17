
def comb_sort(nums: list):
  gap = len(nums)
  swapped = True
  while gap > 1 or swapped:
    gap = max(1, int(gap/1.3))
    swapped = False
    for i in range(len(nums)-gap):
      if nums[i] > nums[i+gap]:
        nums[i], nums[i+gap] = nums[i+gap], nums[i]
        swapped = True
  return nums


