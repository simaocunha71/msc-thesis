def median_numbers(num1: float,num2: float,num3: float) -> float:
  nums = [num1,num2,num3]
  nums.sort()
  if len(nums)%2==0:
    return (nums[1]+nums[2])/2
  else:
    return nums[1]