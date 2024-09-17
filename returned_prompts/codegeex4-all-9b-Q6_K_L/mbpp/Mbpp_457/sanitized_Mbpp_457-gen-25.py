def Find_Min(sublist:list) -> list:
  min_len = min(len(sublist) for sublist in sublist)
  for sublist in sublist:
    if len(sublist) == min_len:
      return sublist