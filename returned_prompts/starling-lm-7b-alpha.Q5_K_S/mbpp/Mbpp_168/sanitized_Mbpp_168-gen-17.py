def frequency(nums:list, target:int) -> int:
  count = 0
  for i in nums:
    if i == target:
      count += 1
  return count