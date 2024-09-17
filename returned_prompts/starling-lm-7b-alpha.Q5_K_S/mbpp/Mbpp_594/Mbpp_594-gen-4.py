
def diff_even_odd(nums: list) -> int:
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      even_num = nums[i]
      break
  for i in range(len(nums)):
    if nums[i] % 2 != 0:
      odd_num = nums[i]
      break
  return odd_num - even_num


