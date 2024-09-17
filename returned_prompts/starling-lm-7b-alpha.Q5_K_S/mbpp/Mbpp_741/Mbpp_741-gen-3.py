
def all_Characters_Same(s: str) -> bool:
  if len(s) == 1:
    return True
  else:
    for i in range(len(s)-1):
      if s[i] != s[i+1]:
        return False
    return True


