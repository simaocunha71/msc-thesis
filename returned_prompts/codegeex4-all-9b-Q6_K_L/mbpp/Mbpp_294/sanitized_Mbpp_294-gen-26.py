def max_val(heterogeneous_list):
  return max(heterogeneous_list, key=lambda x: x if isinstance(x, int) else 0)