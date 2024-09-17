def Find_Min(list1):
  min_len = min(len(sublist) for sublist in list1)
  return [sublist for sublist in list1 if len(sublist) == min_len][0]