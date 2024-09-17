def find_substring(strings: list, sub: str) -> bool:
  for s in strings:
    if sub in s:
      return True
  return False