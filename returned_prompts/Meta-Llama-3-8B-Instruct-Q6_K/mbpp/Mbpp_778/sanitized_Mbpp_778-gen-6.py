def pack_consecutive_duplicates(lst):
  result = [[num] for num in set(lst)]
  for num in lst:
    if num in result[-1]:
      result[-1].append(num)
    else:
      result.append([num])
  return result