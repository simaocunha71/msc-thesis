
def number_of_substrings(s: str) -> int:
  length = len(s)
  return length * (length + 1) // 2


