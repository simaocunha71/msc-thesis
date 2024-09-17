
def check_min_heap(nums: list) -> bool:
  for i in range(len(nums)//2):
    parent = (i+1)//2
    if nums[parent] > nums[i*2+1]:
      return False
    if nums[parent] > nums[i*2+2]:
      return False
  return True


