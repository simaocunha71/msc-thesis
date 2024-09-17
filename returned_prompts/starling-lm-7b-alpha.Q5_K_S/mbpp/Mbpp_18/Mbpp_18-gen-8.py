
def remove_dirty_chars(str1: str, str2: str) -> str:
  return "".join([i for i in str1 if i not in str2])


