
def sample_nam(names: list) -> int:
  sum_of_lengths = 0
  for name in names:
    if name[0] == name[0].lower():
      continue
    sum_of_lengths += len(name)
  return sum_of_lengths


