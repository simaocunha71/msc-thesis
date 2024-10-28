
def sum_Of_Subarray_Prod(nums):
  result = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      result += (prod(nums[i:j+1]))
  return result


