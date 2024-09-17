def max_val(lst):
  max_value = None
  for item in lst:
    if isinstance(item, int) and (max_value is None or item > max_value):
      max_value = item
  return max_value