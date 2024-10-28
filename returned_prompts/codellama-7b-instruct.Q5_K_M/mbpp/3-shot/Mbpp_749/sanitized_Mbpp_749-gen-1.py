def sort_numeric_strings(num_strs: list) -> list:
  return sorted(num_strs, key=lambda s: [int(t) for t in s.split()])