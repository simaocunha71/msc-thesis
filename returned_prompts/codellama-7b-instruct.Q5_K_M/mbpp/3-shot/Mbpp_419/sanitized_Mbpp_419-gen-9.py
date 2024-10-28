def round_and_sum(nums: list) -> float:
  total = 0
  for num in nums:
    rounded_num = round(num)
    total += rounded_num
  return total * len(nums)