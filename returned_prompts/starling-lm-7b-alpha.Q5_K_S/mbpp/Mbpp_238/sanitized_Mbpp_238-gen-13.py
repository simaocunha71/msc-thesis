def number_of_substrings(s: str) -> int:
  length = len(s)
  if length == 0:
    return 0
  return (length * (length + 1)) // 2