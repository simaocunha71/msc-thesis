def mul_even_odd(lst):
  even_nums = [num for num in lst if num % 2 == 0]
  odd_nums = [num for num in lst if num % 2 != 0]
  if len(even_nums) == 0:
    return 0
  elif len(odd_nums) == 0:
    return 0
  else:
    return even_nums[0] * odd_nums[0]  # assuming the first even and odd numbers in the list