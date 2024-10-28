
def dict_depth(d: dict) -> int:
  depth = 0
  for key in d:
    if isinstance(d[key], dict):
      depth = max(depth, dict_depth(d[key])+1)
  return depth


