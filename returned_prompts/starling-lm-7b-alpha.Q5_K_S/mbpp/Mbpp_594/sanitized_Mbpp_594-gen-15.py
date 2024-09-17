def diff_even_odd(nums:list) -> int:
  for i in range(len(nums)):
    if nums[i] % 2 != 0:
      break
  for j in range(len(nums)):
    if nums[j] % 2 == 0:
      break
  return nums[i] - nums[j]