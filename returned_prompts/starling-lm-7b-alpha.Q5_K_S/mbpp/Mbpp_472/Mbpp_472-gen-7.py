
def check_Consecutive(nums:list) -> bool:
  nums.sort()
  for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
      return False
  return True


