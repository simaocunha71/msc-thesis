
def remove_dirty_chars(str1, str2):
  clean_str = ""
  for char in str1:
    if char not in str2:
      clean_str += char
  return clean_str


