def cummulative_sum(nums: list) -> int:
  return sum(sum(i) for i in nums)