def sample_nam(nam):
  total = 0
  for name in nam:
    if not name[0].islower():
      total += len(name)
  return total