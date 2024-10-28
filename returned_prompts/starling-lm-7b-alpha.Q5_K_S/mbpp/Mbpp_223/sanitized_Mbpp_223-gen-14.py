def is_majority(nums:list, n:int, ele:int) -> bool:
  l = 0
  r = n-1
  while l<r:
    if nums[l] == ele:
      l+=1
    if nums[r] == ele:
      r-=1
    if l>r:
      break
    nums[l],nums[r] = nums[r],nums[l]
  if nums.count(ele) > n/2:
    return True
  else:
    return False