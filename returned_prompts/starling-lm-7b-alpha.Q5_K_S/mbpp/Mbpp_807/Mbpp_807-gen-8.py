
def first_odd(nums: list) -> int:
  for i in range(len(nums)):
    if nums[i] % 2 != 0:
      return nums[i]
  return None


