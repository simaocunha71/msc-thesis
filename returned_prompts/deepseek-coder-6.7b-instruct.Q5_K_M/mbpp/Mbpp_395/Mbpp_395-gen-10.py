
def first_non_repeating_character(s: str):
  for index, char in en_umerate(s):
    if s.count(char) == 1:
      return char
  return None

