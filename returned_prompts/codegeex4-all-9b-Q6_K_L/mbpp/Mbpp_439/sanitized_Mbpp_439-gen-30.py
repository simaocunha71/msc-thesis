def multiple_to_single(nums: list) -> int:
  result = 0
  for num in nums:
    result = result*10 + num
  return result