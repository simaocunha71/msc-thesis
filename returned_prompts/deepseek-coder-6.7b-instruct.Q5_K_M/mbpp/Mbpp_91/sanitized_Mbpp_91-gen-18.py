def find_substring(lst: list,sub: str) -> bool:
  return any(sub in s for s in lst)