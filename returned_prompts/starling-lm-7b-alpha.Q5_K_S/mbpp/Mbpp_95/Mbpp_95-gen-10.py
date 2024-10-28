
def Find_Min_Length(lst:list)->int:
  min_len = len(lst[0])
  for i in lst:
    if len(i) < min_len:
      min_len = len(i)
  return min_len


