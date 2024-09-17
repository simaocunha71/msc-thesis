def pack_consecutive_duplicates(nums:list)->list:
  result = []
  curr = []
  for elem in nums:
    if len(curr) == 0:
      curr.append(elem)
    elif curr[-1] == elem:
      curr.append(elem)
    else:
      result.append(curr)
      curr = [elem]
  result.append(curr)
  return result