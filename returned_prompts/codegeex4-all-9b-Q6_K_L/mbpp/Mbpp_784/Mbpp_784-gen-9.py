def mul_even_odd(nums: list) -> int:
  odd_product = 1
  even_product = 1
  for i in nums:
    if i % 2 == 0:
      even_product *= i
    else:
      odd_product *= i
  return odd_product * even_product

