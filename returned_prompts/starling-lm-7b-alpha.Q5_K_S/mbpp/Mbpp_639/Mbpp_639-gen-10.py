
def sample_nam(namz: list) -> int:
  count = 0
  for name in namz:
    if name[0].isupper():
      count += len(name)
  return count


