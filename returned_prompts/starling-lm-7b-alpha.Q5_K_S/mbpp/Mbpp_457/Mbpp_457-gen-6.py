
def Find_Min(sublist:list) -> list:
  min_len = len(sublist[0])
  for i in sublist:
    if len(i) < min_len:
      min_len = len(i)
  return [i for i in sublist if len(i) == min_len]


