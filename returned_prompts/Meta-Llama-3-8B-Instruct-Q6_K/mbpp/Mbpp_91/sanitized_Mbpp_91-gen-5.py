def find_substring(lst: list, substring: str) -> bool:
  for s in lst:
    if substring in s:
      return True
  return False