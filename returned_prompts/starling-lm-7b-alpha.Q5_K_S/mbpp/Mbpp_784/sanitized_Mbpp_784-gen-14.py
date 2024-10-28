def mul_even_odd(nums: list) -> int:
  even_nums = list(filter(lambda x: x%2==0, nums))
  odd_nums = list(filter(lambda x: x%2!=0, nums))
  if len(even_nums) == 0:
    return mul_even_odd(odd_nums)
  elif len(odd_nums) == 0:
    return mul_even_odd(even_nums)
  else:
    return even_nums[0]*odd_nums[0]