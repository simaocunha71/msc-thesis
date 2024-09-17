
def sum_Of_Subarray_Prod(nums: list) -> int:
  n = len(nums)
  prod = 1
  ans = 0
  for i in range(0, n):
    prod = 1
    for j in range(i, n):
      prod *= nums[j]
      ans += prod
  return ans


