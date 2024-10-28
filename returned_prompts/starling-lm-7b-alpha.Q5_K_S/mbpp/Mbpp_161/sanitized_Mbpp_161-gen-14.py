def remove_elements(nums: list, nums2: list) -> list:
  for i in nums2:
    nums.remove(i)
  return nums