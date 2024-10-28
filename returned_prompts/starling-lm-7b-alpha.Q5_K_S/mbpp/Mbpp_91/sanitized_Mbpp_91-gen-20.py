def find_substring(strings: list,substring: str) -> bool:
  for s in strings:
    if substring in s:
      return True
  return False