def find_substring(lst: list,sub_str: str) -> bool:
  for i in lst:
    if sub_str in i:
      return True
  return False