
def issort_list(nums:list)->bool:
  for i in range(len(nums)-1):
    if nums[i+1]<nums[i]:
      return False
  return True


