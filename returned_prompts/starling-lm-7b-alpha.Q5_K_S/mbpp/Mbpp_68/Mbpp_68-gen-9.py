
def is_Monotonic(nums:list)->bool:
  inc = False
  dec = False
  for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
      inc = True
    elif nums[i] > nums[i+1]:
      dec = True
  if inc and dec:
    return False
  elif inc or dec:
    return True
  else:
    return True


