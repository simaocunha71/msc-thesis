def first_non_repeating_character(string: str):
  for index, char in en_umerate(string):
    if string.count(char) == 1:
      return char
  return None