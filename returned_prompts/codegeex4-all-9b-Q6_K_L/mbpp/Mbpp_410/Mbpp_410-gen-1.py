def min_val(het_list):
  min_val = min(het_list, key=lambda x: int(x))
  return int(min_val)