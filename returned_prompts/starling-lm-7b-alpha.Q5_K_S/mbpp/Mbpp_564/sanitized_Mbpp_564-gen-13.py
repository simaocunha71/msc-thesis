def count_Pairs(nums: list,n: int) -> int:
  if len(nums) < n:
    return 0
  else:
    count = 0
    for i in range(len(nums)-1):
      for j in range(i+1, len(nums)):
        if nums[i] != nums[j]:
          count += 1
    return count