def round_and_sum(nums):
  round_nums = [round(num) for num in nums]
  total = sum(round_nums)
  return total