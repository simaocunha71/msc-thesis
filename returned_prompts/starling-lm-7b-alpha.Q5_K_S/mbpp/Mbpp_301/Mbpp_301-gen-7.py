
def dict_depth(d: dict)-> int:
  depth = 0
  for key, value in d.items():
    if isinstance(value, dict):
      depth = max(depth, dict_depth(value)+1)
  return depth


