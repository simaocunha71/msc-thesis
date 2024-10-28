
def odd_position(nums:list) -> bool:
  for i in range(len(nums)):
    if i % 2 == 0:
      if not nums[i] % 2:
        return False
  return True


