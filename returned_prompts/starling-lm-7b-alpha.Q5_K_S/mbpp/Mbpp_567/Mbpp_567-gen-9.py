
def issort_list(nums: list):
  for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
      return False
  return True


