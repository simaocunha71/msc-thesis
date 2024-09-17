
def Find_Min(lst):
  min_len = len(lst[0])
  min_lst = lst[0]
  for i in lst:
    if len(i) < min_len:
      min_len = len(i)
      min_lst = i
  return min_lst


