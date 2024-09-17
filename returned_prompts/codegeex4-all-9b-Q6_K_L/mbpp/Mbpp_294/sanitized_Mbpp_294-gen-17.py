def max_val(lst):
  max_value = max(lst, key=lambda x: x if isinstance(x, int) else -float('inf'))
  return max_value