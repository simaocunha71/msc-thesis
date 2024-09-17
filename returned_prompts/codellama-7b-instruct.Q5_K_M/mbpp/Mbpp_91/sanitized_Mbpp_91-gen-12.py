def find_substring(my_list: list,substring: str) -> bool:
  for i in my_list:
    if substring in i:
      return True
  return False