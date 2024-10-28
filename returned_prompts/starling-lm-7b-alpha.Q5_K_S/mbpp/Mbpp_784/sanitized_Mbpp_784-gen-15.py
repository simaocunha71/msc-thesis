def mul_even_odd(nums:list) -> int:
  even_nums = [num for num in nums if num%2 == 0]
  odd_nums = [num for num in nums if num%2 != 0]
  if len(even_nums) == 0:
    return odd_nums[0]
  elif len(odd_nums) == 0:
    return even_nums[0]
  else:
    return even_nums[0]*odd_nums[0]