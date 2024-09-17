
def dict_depth(dct: dict) -> int:
  if not dct:
    return 0

  max_depth = 0
  for key, value in dct.items():
      depth = 1
      if isinstance(value, dict):
          depth += dict_depth(value)
      max_depth = max(max_depth, depth)

  return max_depth


