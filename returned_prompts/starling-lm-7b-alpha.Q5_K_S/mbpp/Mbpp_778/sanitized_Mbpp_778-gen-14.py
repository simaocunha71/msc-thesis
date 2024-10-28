def pack_consecutive_duplicates(nums):
  result = []
  curr = []
  for i in nums:
    if len(curr) == 0:
      curr.append(i)
    elif curr[-1] != i:
      result.append(curr)
      curr = [i]
    else:
      curr.append(i)
  result.append(curr)
  return result