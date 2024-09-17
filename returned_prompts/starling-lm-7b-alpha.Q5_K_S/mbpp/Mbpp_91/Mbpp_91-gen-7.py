
def find_substring(strings: list,substring: str) -> bool:
  for string in strings:
    if substring in string:
      return True
  return False


