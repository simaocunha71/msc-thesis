def mul_even_odd(nums):
  result = 1
  for num in nums:
    if num % 2 == 0:
      result *= num
    else:
      result *= num
  return result