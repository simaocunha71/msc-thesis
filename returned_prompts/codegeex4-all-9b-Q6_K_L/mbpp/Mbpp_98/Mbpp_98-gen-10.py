def multiply_num(nums):
  mul = 1
  for i in nums:
    mul *= i
  return mul/len(nums)