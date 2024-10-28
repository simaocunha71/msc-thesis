def smallest_num(lst):
  if not lst:
    return None
  try:
    return min(lst)
  except TypeError:
    return None