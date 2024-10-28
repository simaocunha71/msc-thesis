def pack_consecutive_duplicates(nums: list) -> list:
  result = []
  current = []
  for num in nums:
    if not current or current[-1] != num:
      if current:
        result.append(current)
      current = [num]
    else:
      current.append(num)
  result.append(current)
  return result

