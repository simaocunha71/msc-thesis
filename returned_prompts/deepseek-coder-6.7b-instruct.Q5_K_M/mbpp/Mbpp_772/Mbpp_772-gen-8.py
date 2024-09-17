
def remove_length(s: str, k: int) -> str:
  return ' '.join([w for w in s.split() if len(w) != k])


