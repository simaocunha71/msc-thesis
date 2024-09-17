def all_Characters_Same(s: str) -> bool:
  if len(s) == 0:
    return False
  return len(set(s)) == 1