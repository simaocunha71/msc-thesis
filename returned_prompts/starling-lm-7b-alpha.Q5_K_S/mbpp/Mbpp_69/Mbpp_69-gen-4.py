
def is_sublist(nums,sub_nums):
  for i in range(len(nums)-len(sub_nums)+1):
    if nums[i:i+len(sub_nums)]==sub_nums:
      return True
  return False


