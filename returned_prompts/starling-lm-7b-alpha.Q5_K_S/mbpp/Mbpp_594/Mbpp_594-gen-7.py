
def diff_even_odd(nums:list)->int:
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      first_even = nums[i]
      break
  for i in range(len(nums)):
    if nums[i] % 2 != 0:
      first_odd = nums[i]
      break
  return first_odd - first_even


