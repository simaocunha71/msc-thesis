def sample_nam(names: list) -> int:
  length = 0
  for name in names:
    if name[0].isupper():
      length += len(name)
  return length