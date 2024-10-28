def find_substring(strings: list, sub_str: str) -> bool:
  for string in strings:
    if sub_str in string:
      return True
  return False