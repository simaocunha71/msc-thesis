
def sum_Of_Subarray_Prod(nums):
  def subarray_prod(nums):
    prod = 1
    for i in nums:
      prod *= i
    return prod

  def subarrays(nums):
    n = len(nums)
    for i in range(n):
      for j in range(i,n):
        yield nums[i:j+1]

  return sum(subarray_prod(subarray) for subarray in subarrays(nums))


