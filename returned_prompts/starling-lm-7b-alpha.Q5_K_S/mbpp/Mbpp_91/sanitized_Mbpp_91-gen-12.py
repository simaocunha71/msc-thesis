def find_substring(strings: list, substr: str) -> bool:
  for string in strings:
    if substr in string:
      return True
  return False