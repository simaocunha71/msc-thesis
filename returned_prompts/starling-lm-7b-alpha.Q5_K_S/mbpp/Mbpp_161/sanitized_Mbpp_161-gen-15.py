def remove_elements(nums: list,rem: list) -> list:
  for i in rem:
    while i in nums:
      nums.remove(i)
  return nums