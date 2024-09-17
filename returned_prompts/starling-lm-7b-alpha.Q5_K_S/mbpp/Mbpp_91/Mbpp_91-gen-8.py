
def find_substring(words: list, sub: str) -> bool:
  for w in words:
    if sub in w:
      return True
  return False


