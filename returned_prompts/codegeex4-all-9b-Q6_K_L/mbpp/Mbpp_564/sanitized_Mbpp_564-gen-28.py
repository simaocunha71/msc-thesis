def count_Pairs(nums: list, n: int) -> int:
  nums_set = set(nums)
  count = 0
  for num in nums_set:
    count += nums.count(num) - 1
  return count