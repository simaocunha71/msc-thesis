def sample_nam(names: list) -> int:
  filtered_names = [name for name in names if not name.lower().startswith('a')]
  return sum(len(name) for name in filtered_names)