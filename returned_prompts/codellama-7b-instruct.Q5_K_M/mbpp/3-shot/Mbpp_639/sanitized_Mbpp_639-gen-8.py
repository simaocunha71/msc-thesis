def sample_nam(names: list) -> int:
  sum_of_len = 0
  for name in names:
    if not name[0].islower():
      sum_of_len += len(name)
  return sum_of_len