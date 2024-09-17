def remove_dirty_chars(string, chars):
  for char in chars:
    string = string.replace(char, '')
  return string