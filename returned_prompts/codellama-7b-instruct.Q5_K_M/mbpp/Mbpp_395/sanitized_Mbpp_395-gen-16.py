def first_non_repeating_character(input_string: str) -> str:
  for char in input_string:
    if input_string.count(char) == 1:
      return char
  return None