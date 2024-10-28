def is_sublist(nums:list,sub_nums:list)->bool:
  for i in range(len(nums)-len(sub_nums)+1):
    if nums[i:i+len(sub_nums)]==sub_nums:
      return True
  return False