def last(nums: list, n: int) -> int:
  for i in range(len(nums)-1, -1, -1):
    if nums[i] == n:
      return i
  return -1