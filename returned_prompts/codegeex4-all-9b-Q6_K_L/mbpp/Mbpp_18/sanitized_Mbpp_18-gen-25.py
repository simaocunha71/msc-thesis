def remove_dirty_chars(str1, str2):
  return "".join([char for char in str1 if char not in str2])