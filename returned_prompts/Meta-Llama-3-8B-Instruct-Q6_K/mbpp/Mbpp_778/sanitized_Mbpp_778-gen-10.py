def pack_consecutive_duplicates(lst):
  result = [[x] for x in lst]
  for i in range(len(result) - 1):
    if result[i][0] == result[i+1][0]:
      result[i].append(result[i+1].pop(0))
  return result