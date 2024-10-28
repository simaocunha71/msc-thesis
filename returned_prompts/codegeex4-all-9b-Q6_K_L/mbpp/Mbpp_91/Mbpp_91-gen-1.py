def find_substring(list_of_strings: list, substring: str) -> bool:
  for string in list_of_strings:
    if substring in string:
      return True
  return False