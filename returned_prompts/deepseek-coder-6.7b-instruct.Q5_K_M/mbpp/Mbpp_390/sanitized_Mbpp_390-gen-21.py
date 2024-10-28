def add_string(lst: list, fmt_str: str) -> list:
  return [fmt_str.format(i) for i in lst]