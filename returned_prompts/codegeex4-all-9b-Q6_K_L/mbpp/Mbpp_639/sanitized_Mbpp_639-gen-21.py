def sample_nam(names: list) -> int:
  sum_len = 0
  for name in names:
    if name[0].isupper():
      sum_len += len(name)
  return sum_len