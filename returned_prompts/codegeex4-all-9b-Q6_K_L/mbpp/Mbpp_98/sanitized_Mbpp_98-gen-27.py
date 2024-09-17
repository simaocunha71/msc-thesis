def multiply_num(nums: list):
  product = 1
  for num in nums:
    product *= num
  return product / len(nums)