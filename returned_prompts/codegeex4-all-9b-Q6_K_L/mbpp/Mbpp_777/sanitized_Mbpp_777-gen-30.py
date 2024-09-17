def find_sum(nums: list) -> int:
  sum = 0
  for num in nums:
    if nums.count(num) == 1:
      sum += num
  return sum