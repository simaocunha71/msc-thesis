def find_substring(lst: list, string: str) -> bool:
  for item in lst:
    if string in item:
      return True
  return False