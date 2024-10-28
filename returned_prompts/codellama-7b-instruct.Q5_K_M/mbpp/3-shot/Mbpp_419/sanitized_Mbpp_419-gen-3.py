def round_and_sum(nums: list) -> int:
  total_sum = 0
  for num in nums:
    rounded_num = round(num)
    total_sum += rounded_num
  return total_sum