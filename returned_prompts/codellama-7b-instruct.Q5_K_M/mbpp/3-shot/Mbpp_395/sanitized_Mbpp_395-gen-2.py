def first_non_repeating_character(str):
  for char in str:
    if str.count(char) == 1:
      return char
  return None