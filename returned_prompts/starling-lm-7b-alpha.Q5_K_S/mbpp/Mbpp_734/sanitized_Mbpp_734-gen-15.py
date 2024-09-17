def sum_Of_Subarray_Prod(nums):
  return sum(i*j for i, j in zip(nums, nums[1:])) + sum(nums[i]*nums[i+1]*nums[i+2] for i in range(len(nums)-2))