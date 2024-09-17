
def sample_nam(names: list) -> int:
  names_len = 0
  for name in names:
    if name[0].isupper():
      names_len += len(name)
  return names_len


