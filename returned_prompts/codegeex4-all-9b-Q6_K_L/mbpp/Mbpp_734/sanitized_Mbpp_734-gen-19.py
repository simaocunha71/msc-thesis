def sum_Of_Subarray_Prod(nums: list) -> int:
  if len(nums) == 0:
    return 0

  total = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      total += prod(nums[i:j+1])
  return total
def prod(nums: list) -> int:
  product = 1
  for num in nums:
    product *= num
  return product