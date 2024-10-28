def mul_even_odd(nums: list):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return nums[count-1] * nums[count]

