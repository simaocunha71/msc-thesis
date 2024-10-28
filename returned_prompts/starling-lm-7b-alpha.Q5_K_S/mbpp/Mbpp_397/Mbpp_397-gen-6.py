
def median_numbers(*nums: float) -> float:
  nums = sorted(nums)
  if len(nums) % 2 == 0:
    return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
  else:
    return nums[len(nums)//2]


