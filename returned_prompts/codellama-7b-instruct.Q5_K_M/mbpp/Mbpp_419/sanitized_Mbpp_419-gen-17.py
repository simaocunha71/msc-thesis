def round_and_sum(nums: list):
  total_sum = 0
  for num in nums:
    num = round(num)
    total_sum += num
  return total_sum * len(nums)