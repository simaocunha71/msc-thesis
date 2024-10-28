def number_of_substrings(string: str) -> int:
  return sum(len(string) - i for i in range(len(string)))