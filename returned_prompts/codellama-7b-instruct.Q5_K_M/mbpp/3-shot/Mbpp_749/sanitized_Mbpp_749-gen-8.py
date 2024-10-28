def sort_numeric_strings(my_list: list) -> list:
  return sorted(my_list, key=lambda s: [int(t) if t.isdigit() else t for t in s])