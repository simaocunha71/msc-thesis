def find_substring(lst: list, substr: str) -> bool:
  for item in lst:
    if substr in item:
      return True
  return False