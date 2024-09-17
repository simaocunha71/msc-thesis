
def dict_depth(d):
  depth = 0
  for k, v in d.items():
    depth = max(depth, dict_depth(v)+1)
  return depth


