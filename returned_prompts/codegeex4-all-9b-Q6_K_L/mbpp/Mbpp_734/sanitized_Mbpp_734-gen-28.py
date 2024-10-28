def sum_Of_Subarray_Prod(nums: list) -> int:
  total_sum = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
      subarray = nums[i:j]
      total_sum += prod(subarray)
  return total_sum
def prod(nums: list) -> int:
  product = 1
  for num in nums:
    product *= num
  return product