
def find_substring(my_list: list,substring: str) -> bool:
  for s in my_list:
    if substring in s:
      return True
  return False


