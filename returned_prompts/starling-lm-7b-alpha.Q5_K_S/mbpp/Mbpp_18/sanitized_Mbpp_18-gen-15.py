def remove_dirty_chars(string_1, string_2):
  for char in string_2:
    string_1 = string_1.replace(char, '')
  return string_1