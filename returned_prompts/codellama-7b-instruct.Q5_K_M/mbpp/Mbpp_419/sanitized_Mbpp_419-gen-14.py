def round_and_sum(nums: list) -> int:
  total = 0
  for num in nums:
    num = round(num)
    total += num
  return total * len(nums)