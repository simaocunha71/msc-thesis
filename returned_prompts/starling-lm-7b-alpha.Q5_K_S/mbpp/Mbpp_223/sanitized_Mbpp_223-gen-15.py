def is_majority(nums: list,n: int,ele: int) -> bool:
  if nums.count(ele) > n/2:
    return True
  else:
    return False