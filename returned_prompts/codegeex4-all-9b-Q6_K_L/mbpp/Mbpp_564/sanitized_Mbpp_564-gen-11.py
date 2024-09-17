def count_Pairs(nums: list,n: int) -> int:
  count = 0
  for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
      count += 1
  return count