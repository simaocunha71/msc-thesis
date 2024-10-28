def min_val(lst):
  min_num = None
  for i in lst:
    if isinstance(i, int) or isinstance(i, float):
      if min_num is None:
        min_num = i
      else:
        min_num = min(min_num, i)
  return min_num

