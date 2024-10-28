
def find_substring(my_list: list, substring: str) -> bool:
  for word in my_list:
    if substring in word:
      return True
  return False


