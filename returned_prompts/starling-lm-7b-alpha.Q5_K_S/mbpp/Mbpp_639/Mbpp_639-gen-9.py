
def sample_nam(names: list):
  sum_len = 0
  for name in names:
    if name[0] != 'd':
      sum_len += len(name)
  return sum_len


