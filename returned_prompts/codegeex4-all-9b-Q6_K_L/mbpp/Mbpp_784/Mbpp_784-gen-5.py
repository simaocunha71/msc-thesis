def mul_even_odd(nums: list):
  mul = 1
  for i in range(len(nums)):
    if i % 2 == 0:
      mul *= nums[i]
    else:
      mul *= nums[i]
  return mul

