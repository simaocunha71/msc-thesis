def sum_Of_Subarray_Prod(nums):
  n = len(nums)
  sum_of_products = 0
  for i in range(n):
    product = 1
    for j in range(i, n):
      product *= nums[j]
      sum_of_products += product
  return sum_of_products