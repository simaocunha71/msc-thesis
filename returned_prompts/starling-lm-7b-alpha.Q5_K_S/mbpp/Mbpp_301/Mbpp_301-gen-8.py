
def dict_depth(d):
  return 1 + max(map(dict_depth, d.values())) if isinstance(d, dict) else 0


