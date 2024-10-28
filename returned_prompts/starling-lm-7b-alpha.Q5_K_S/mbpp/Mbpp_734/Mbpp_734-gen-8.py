
def sum_Of_Subarray_Prod(nums: list) -> int:
  res = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      res += sum(nums[i:j+1])
  return res


