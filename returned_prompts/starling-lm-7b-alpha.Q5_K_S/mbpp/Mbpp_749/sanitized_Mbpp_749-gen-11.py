def sort_numeric_strings(num_strings: list) -> list:
  return sorted(num_strings, key=lambda s: int(s))