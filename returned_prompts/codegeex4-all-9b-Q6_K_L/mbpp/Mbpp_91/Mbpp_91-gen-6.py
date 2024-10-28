def find_substring(list_values: list,sub_str: str) -> bool:
  for value in list_values:
    if sub_str in value:
      return True
  return False

