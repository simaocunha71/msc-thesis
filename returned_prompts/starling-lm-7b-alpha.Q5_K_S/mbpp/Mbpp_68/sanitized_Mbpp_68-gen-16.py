def is_Monotonic(nums):
  inc = False
  dec = False
  for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
      inc = True
    if nums[i] > nums[i+1]:
      dec = True
  if inc and not dec:
    return True
  if not inc and dec:
    return True
  return False