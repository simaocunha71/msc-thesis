def find_Max_Num(nums: list) -> int:
  nums.sort()
  max_num = 0
  for i in range(len(nums)):
    max_num = max(max_num, nums[len(nums)-1-i] * 10**i)
  return max_num