def round_and_sum(nums):
  total_sum = sum(round(num) for num in nums)
  return total_sum * len(nums)