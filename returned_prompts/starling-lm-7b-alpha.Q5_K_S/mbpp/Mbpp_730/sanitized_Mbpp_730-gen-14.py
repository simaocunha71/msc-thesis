def consecutive_duplicates(nums):
  prev = None
  result = []
  for num in nums:
    if num == prev:
      continue
    result.append(num)
    prev = num
  return result