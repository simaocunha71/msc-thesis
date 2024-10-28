
def number_of_substrings(s: str) -> int:
  return sum(s[:i+1] for i in range(len(s)))


