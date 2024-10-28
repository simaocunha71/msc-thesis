def sum_Of_Subarray_Prod(nums: list) -> int:
  total = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      product = 1
      for k in range(i, j + 1):
        product *= nums[k]
      total += product
  return total

