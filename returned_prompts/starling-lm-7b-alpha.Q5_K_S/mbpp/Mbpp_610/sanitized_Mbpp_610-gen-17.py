def remove_kth_element(nums:list,k:int)->list:
  nums_len = len(nums)
  if nums_len<k:
    return []
  else:
    return nums[:k]+nums[k+1:]