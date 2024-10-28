def diff_even_odd(nums:list):
  even_nums = [num for num in nums if num % 2 == 0]
  odd_nums = [num for num in nums if num % 2 != 0]
  if len(even_nums) > 0 and len(odd_nums) > 0:
    return even_nums[0] - odd_nums[0]
  else:
    return None