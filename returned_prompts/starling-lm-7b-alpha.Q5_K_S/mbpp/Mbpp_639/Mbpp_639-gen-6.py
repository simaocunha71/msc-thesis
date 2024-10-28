
def sample_nam(names:list):
  sum_length = 0
  for name in names:
    if name[0] != "d" and name[0] != "D":
      sum_length += len(name)
  return sum_length


