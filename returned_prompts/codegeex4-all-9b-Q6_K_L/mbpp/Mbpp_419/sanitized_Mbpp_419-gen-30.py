def round_and_sum(nums):
  nums = [round(num) for num in nums]
  total = sum(nums)
  return total * len(nums)