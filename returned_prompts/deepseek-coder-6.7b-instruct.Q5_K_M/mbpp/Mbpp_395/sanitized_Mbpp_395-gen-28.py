def first_non_repeating_character(string):
  for index, char in en_umerate(string):
    if string.count(char) == 1:
      return char
  return None