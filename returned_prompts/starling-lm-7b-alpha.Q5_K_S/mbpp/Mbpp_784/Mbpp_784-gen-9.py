
def mul_even_odd(nums: list) -> int:
  even_nums = [x for x in nums if x % 2 == 0]
  odd_nums = [x for x in nums if x % 2 != 0]
  if len(even_nums) == 0:
    return 0
  elif len(odd_nums) == 0:
    return even_nums[0]
  else:
    return even_nums[0] * odd_nums[0]


