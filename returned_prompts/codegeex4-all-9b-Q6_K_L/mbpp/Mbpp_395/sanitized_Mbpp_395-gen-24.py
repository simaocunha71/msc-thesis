def first_non_repeating_character(s: str):
  for char in s:
    if s.count(char) == 1:
      return char
  return None