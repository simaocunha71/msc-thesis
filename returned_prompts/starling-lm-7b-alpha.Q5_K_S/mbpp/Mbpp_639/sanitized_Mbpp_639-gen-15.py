def sample_nam(nam:list) -> int:
  nam_len = 0
  for name in nam:
    if name[0] == name[0].upper():
      nam_len += len(name)
  return nam_len