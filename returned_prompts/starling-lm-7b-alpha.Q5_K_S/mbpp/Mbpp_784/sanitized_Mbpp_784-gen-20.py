def mul_even_odd(nums:list) -> int:
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      even = nums[i]
      break
  for i in range(len(nums)):
    if nums[i] % 2 != 0:
      odd = nums[i]
      break
  return even * odd