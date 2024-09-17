def mul_even_odd(nums):
  even_product = 1
  odd_product = 1
  for num in nums:
    if num % 2 == 0:
      even_product *= num
    else:
      odd_product *= num
  return even_product, odd_product