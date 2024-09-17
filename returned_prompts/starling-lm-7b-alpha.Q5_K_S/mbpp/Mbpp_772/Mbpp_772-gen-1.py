
def remove_length(s: str, k: int) -> str:
  return ' '.join([i for i in s.split() if len(i)!=k])


