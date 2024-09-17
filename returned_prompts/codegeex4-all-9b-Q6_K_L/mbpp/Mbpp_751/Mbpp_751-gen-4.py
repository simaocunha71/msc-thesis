def check_min_heap(nums: list) -> bool:
  for i in range(len(nums)):
    left = 2*i + 1
    right = 2*i + 2
    if left < len(nums) and nums[i] > nums[left]:
      return False
    if right < len(nums) and nums[i] > nums[right]:
      return False
  return True

