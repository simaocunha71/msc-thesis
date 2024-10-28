
def sum_Of_Subarray_Prod(nums: list) -> int:
  total = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
      total += reduce(lambda x, y: x*y, nums[i:j])
  return total


