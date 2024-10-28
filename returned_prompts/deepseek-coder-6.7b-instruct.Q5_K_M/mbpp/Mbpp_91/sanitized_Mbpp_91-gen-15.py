def find_substring(lst: list, substring: str) -> bool:
  return any(substring in s for s in lst)