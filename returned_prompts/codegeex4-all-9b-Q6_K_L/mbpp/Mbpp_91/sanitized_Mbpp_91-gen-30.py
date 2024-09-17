def find_substring(lst: list, substring: str) -> bool:
  for word in lst:
    if substring in word:
      return True
  return False