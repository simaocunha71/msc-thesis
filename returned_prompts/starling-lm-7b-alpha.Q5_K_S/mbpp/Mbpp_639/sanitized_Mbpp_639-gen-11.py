def sample_nam(names: list) -> int:
  names = [name for name in names if name[0] != name[0].lower()]
  return sum([len(name) for name in names])