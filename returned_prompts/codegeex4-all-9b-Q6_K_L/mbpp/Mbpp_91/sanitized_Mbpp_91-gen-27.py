def find_substring(lst: list, substring: str) -> bool:
  for i in lst:
    if substring in i:
      return True
  return False