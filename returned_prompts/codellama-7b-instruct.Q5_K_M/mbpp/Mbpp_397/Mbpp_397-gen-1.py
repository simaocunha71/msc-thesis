
def median_numbers(num1: float, num2: float, num3: float) -> float:
  nums = sorted([num1, num2, num3])
  length = len(nums)
  if length%2==0:
    median = (nums[length//2]+nums[length//2-1])/2
  else:
    median = nums[length//2]
  return median


