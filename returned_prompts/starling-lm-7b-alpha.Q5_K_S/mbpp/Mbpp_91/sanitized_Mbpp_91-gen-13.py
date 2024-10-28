def find_substring(strings: list, sub: str) -> bool:
  for string in strings:
    if sub in string:
      return True
  return False