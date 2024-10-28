
def sum_Of_Subarray_Prod(nums: list) -> int:
  product = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      product += reduce(lambda x, y: x*y, nums[i:j+1])
  return product


