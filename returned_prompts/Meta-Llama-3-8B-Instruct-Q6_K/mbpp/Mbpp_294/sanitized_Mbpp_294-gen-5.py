def max_val(lst):
  return max(map(lambda x: x if isinstance(x, int) else float('inf'), lst))