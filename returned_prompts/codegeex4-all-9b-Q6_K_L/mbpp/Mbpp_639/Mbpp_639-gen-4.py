def sample_nam(names: list) -> int:
  count = 0
  for name in names:
    if name[0].isupper():
      count += len(name)
  return count

