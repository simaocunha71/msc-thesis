def sum_Of_Subarray_Prod(nums: list) -> int:
  result = 0
  for i in range(len(nums)):
    for j in range(len(nums)):
      result += sum(nums[i:j+1])
  return result