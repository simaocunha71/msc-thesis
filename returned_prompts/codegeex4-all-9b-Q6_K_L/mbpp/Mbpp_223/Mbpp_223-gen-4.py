def is_majority(nums: list,n: int,el: int) -> bool:
  count = 0
  for i in range(n):
    if nums[i] == el:
      count += 1
  return count > n/2

