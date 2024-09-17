
def remove_length(s: str, k: int) -> str:
  return ' '.join([word for word in s.split() if len(word) != k])


