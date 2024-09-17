def split_Arr(nums: list, n: int) -> list:
  if n > len(nums):
    return nums
  first_part = nums[:n]
  second_part = nums[n:]
  return second_part + first_part

