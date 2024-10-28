def first_non_repeating_character(string):
  char_count = {}
  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  for char in string:
    if char_count[char] == 1:
      return char
  return None