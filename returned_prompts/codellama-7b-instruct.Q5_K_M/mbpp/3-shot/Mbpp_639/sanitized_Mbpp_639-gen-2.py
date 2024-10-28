def sample_nam(names: list) -> int:
  sum = 0
  for name in names:
    if name[0].isupper():
      sum += len(name)
  return sum